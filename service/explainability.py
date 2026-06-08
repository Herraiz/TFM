"""
Métodos de explicabilidad: Grad-CAM, LIME y SHAP.
Cada función devuelve la imagen resultante codificada en Base64.
"""

import base64
import io

import numpy as np
import tensorflow as tf
import matplotlib.cm as cm
import shap
from PIL import Image
from lime import lime_image
from skimage.segmentation import mark_boundaries, quickshift

from config import (
    GRADCAM_ALPHA,
    LIME_NUM_SAMPLES,
    LIME_NUM_FEATURES,
    LIME_QUICKSHIFT_KERNEL_SIZE,
    LIME_QUICKSHIFT_MAX_DIST,
    LIME_QUICKSHIFT_RATIO,
    SHAP_MAX_EVALS,
    SHAP_BATCH_SIZE,
    SHAP_BLUR_KERNEL,
    CLASSES,
    IMAGE_SIZE,
)


# ---------------------------------------------------------------------------
# Helpers internos
# ---------------------------------------------------------------------------

def _array_to_base64_jpeg(img_array: np.ndarray) -> str:
    """Convierte un array HxWx3 (float o uint8) a JPEG codificado en Base64."""
    pil_img = Image.fromarray(img_array.astype(np.uint8))
    buffered = io.BytesIO()
    pil_img.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")


def _pil_to_base64_jpeg(pil_img: Image.Image) -> str:
    """Convierte una imagen PIL a JPEG codificado en Base64."""
    buffered = io.BytesIO()
    pil_img.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")


def _apply_jet_overlay(heatmap_normalized: np.ndarray, original_img_array: np.ndarray) -> Image.Image:
    """
    Superpone un mapa de calor normalizado [0,1] sobre la imagen original
    usando la paleta 'jet' y el alpha definido en config.

    Args:
        heatmap_normalized: Array 2D con valores en [0, 1].
        original_img_array: Array HxWx3 de la imagen original (valores en [0,255]).

    Returns:
        Imagen PIL con la superposición.
    """
    jet = cm.get_cmap("jet")
    jet_colors = jet(np.arange(256))[:, :3]
    heatmap_uint8 = (heatmap_normalized * 255).astype(int)
    jet_heatmap = jet_colors[heatmap_uint8]

    jet_pil = tf.keras.utils.array_to_img(jet_heatmap).resize(IMAGE_SIZE)
    jet_array = tf.keras.utils.img_to_array(jet_pil)

    superimposed = jet_array * GRADCAM_ALPHA + original_img_array
    return tf.keras.utils.array_to_img(superimposed)


# ---------------------------------------------------------------------------
# Grad-CAM
# ---------------------------------------------------------------------------

def _build_gradcam_submodels(model, last_conv_layer_name: str):
    """
    Construye los sub-modelos necesarios para calcular los gradientes de Grad-CAM.

    Returns:
        Tupla (inner_model, pool_layer, meta_branch, top_model).
    """
    v_model = model.get_layer("coatnet0")
    inner_model = tf.keras.Model(
        inputs=v_model.inputs,
        outputs=[v_model.get_layer(last_conv_layer_name).output, v_model.output],
    )

    pool_layer = next(l for l in model.layers if isinstance(l, tf.keras.layers.GlobalAveragePooling2D))
    concat_layer = next(l for l in model.layers if isinstance(l, tf.keras.layers.Concatenate))
    meta_branch = tf.keras.Model(inputs=model.input[1], outputs=concat_layer.input[1])

    top_input = tf.keras.Input(shape=concat_layer.output.shape[1:])
    x = top_input
    for layer in model.layers[model.layers.index(concat_layer) + 1 :]:
        x = layer(x)
    top_model = tf.keras.Model(inputs=top_input, outputs=x)

    return inner_model, pool_layer, meta_branch, concat_layer, top_model


def get_gradcam_base64(
    img_input: np.ndarray,
    meta_input: np.ndarray,
    model,
    last_conv_layer_name: str,
    pred_index: int,
) -> str:
    """
    Calcula Grad-CAM, superpone el mapa de calor a la imagen original
    y devuelve el resultado codificado en Base64.
    """
    inner_model, pool_layer, meta_branch, concat_layer, top_model = _build_gradcam_submodels(
        model, last_conv_layer_name
    )

    with tf.GradientTape() as tape:
        conv_output, backbone_out = inner_model(img_input)
        x_img = pool_layer(backbone_out)
        x_meta = meta_branch(meta_input)
        combined = concat_layer([x_img, x_meta])
        predictions = top_model(combined)
        class_channel = predictions[:, pred_index]

    grads = tape.gradient(class_channel, conv_output)
    pooled_grads = tf.reduce_mean(grads, axis=(0, 1, 2))
    heatmap = conv_output[0] @ pooled_grads[..., tf.newaxis]
    heatmap = tf.squeeze(heatmap)
    heatmap = tf.maximum(heatmap, 0) / (tf.math.reduce_max(heatmap) + 1e-10)
    heatmap_np = heatmap.numpy()

    original_img_array = tf.keras.utils.img_to_array(
        tf.keras.utils.array_to_img(img_input[0])
    )
    superimposed = _apply_jet_overlay(heatmap_np, original_img_array)
    return _pil_to_base64_jpeg(superimposed)


# ---------------------------------------------------------------------------
# LIME
# ---------------------------------------------------------------------------

_lime_explainer = lime_image.LimeImageExplainer()


def get_lime_base64(img_input: np.ndarray, predict_fn) -> str:
    """
    Genera la explicación LIME para la imagen y la devuelve en Base64.

    Args:
        img_input: Array (1, H, W, 3) normalizado.
        predict_fn: Función wrapper que acepta un batch y devuelve probabilidades.
    """
    exp = _lime_explainer.explain_instance(
        img_input[0].astype(np.double),
        predict_fn,
        top_labels=1,
        num_samples=LIME_NUM_SAMPLES,
        segmentation_fn=lambda x: quickshift(
            x,
            kernel_size=LIME_QUICKSHIFT_KERNEL_SIZE,
            max_dist=LIME_QUICKSHIFT_MAX_DIST,
            ratio=LIME_QUICKSHIFT_RATIO,
        ),
    )
    temp, mask = exp.get_image_and_mask(
        exp.top_labels[0],
        positive_only=True,
        num_features=LIME_NUM_FEATURES,
        hide_rest=False,
    )
    lime_img_array = (mark_boundaries(temp, mask) * 255).astype(np.uint8)
    return _array_to_base64_jpeg(lime_img_array)


# ---------------------------------------------------------------------------
# SHAP
# ---------------------------------------------------------------------------

def get_shap_base64(img_input: np.ndarray, predict_fn, pred_index: int) -> str:
    """
    Genera el mapa SHAP para la clase predicha, lo superpone a la imagen
    original con la paleta 'jet' y devuelve el resultado en Base64.

    Args:
        img_input: Array (1, H, W, 3) normalizado.
        predict_fn: Función wrapper que acepta un batch y devuelve probabilidades.
        pred_index: Índice de la clase predicha.
    """
    masker = shap.maskers.Image(SHAP_BLUR_KERNEL, shape=(*IMAGE_SIZE, 3))
    explainer = shap.Explainer(predict_fn, masker, output_names=CLASSES)
    sv = explainer(img_input, max_evals=SHAP_MAX_EVALS, batch_size=SHAP_BATCH_SIZE)

    shap_map = sv.values[0, :, :, :, pred_index].sum(axis=-1)
    shap_normalized = (shap_map - shap_map.min()) / (shap_map.max() - shap_map.min() + 1e-10)

    original_img_array = tf.keras.utils.img_to_array(
        tf.keras.utils.array_to_img(img_input[0])
    )
    superimposed = _apply_jet_overlay(shap_normalized, original_img_array)
    return _pil_to_base64_jpeg(superimposed)
