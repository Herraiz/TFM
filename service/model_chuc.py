"""
Carga del modelo y preprocesadores, e inferencia.
"""

import joblib
import numpy as np
import tensorflow as tf
from keras_cv_attention_models import coatnet  # Aunque parezca que no se usa, es necesario para deserializar el modelo

from service.config_chuc import (
    MODEL_PATH,
    SCALER_PATH,
    ENCODER_PATH,
    CLASSES,
    CLASS_TRANSLATIONS,
)


def load_preprocessors():
    """Carga scaler y encoder entrenados desde disco."""
    scaler = joblib.load(SCALER_PATH)
    encoder = joblib.load(ENCODER_PATH)
    return scaler, encoder


def load_model():
    """Carga el modelo Keras completo sin compilar (necesario para GradientTape)."""
    return tf.keras.models.load_model(MODEL_PATH, compile=False)


def get_last_conv_layer_name(model) -> str:
    """Detecta automáticamente el nombre de la última capa convolucional del backbone."""
    sub_model = model.get_layer("coatnet0")
    conv_layers = [l.name for l in sub_model.layers if "conv" in l.name.lower()]
    return conv_layers[-1]


def run_inference(model, img_array: np.ndarray, meta_array: np.ndarray) -> dict:
    """
    Ejecuta la inferencia y devuelve un diccionario con scores, clase predicha
    e índice / confianza de la predicción.

    Returns:
        {
            "scores": {nombre_clase: probabilidad, ...},
            "predicted_class": str,
            "pred_index": int,
            "confidence": float,
        }
    """
    raw_scores = model.predict([img_array, meta_array])[0]
    pred_index = int(np.argmax(raw_scores))

    return {
        "scores": {
            CLASS_TRANSLATIONS[cls]: float(score)
            for cls, score in zip(CLASSES, raw_scores)
        },
        "predicted_class": CLASSES[pred_index],
        "pred_index": pred_index,
        "confidence": float(raw_scores[pred_index]),
    }


def make_hybrid_predict_fn(model, meta_array: np.ndarray):
    """
    Devuelve una función de predicción que fija los metadatos y acepta
    únicamente un batch de imágenes, compatible con LIME y SHAP.
    """
    def hybrid_predict(batch: np.ndarray) -> np.ndarray:
        m_batch = np.repeat(meta_array, batch.shape[0], axis=0)
        return model.predict([batch, m_batch], verbose=0)

    return hybrid_predict
