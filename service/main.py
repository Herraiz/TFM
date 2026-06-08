from fastapi import FastAPI, UploadFile, File, Form
import tensorflow as tf
import numpy as np
from PIL import Image
import io
import joblib
import base64
import matplotlib.cm as cm
from keras_cv_attention_models import coatnet # Necesario para cargar el modelo aunque no lo use directamente
from lime import lime_image
from skimage.segmentation import mark_boundaries, quickshift, slic, felzenszwalb, watershed

app = FastAPI()

# Cargo los objetos de preprocesamiento entrenados
try:
    scaler = joblib.load("../models/scaler.pkl")
    encoder = joblib.load("../models/encoder.pkl")
except FileNotFoundError:
    print("Error: No se encontraron los preprocesadores del notebook.")

# Cargo el modelo completo de Keras (tiene que ser el .keraspara poder extraer gradientes)
model = tf.keras.models.load_model("../models/implementation_jesus_1.keras", compile=False)

# Necesito el nombre exacto de la última capa convolucional. Se puede averiguar ejecutando model.summary() en el notebook
sub_model = model.get_layer('coatnet0')
LAST_CONV_LAYER_NAME = [l.name for l in sub_model.layers if 'conv' in l.name.lower()][-1]

print("#" * 50)
print(f"Última capa convolucional detectada: {LAST_CONV_LAYER_NAME}")
print("#" * 50)
print("Valores del encoder:", encoder.get_feature_names_out())
print("#" * 50)

# Para interpretar las predicciones, necesitamos saber el orden de las clases. Tiene que tener mismo orden que en el notebook
classes = ["akiec", "bcc", "bkl", "df", "nv", "mel", "vasc"]
translations = {  
    # Mapeo para códigos cortos a nombres completos
    'akiec': 'Queratosis actínica (akiec)',
    'bcc': 'Carcinoma basocelular (bcc)',
    'bkl': 'Queratosis benigna (bkl)',
    'df': 'Dermatofibroma (df)',
    'nv': 'Nevus melanocítico (nv)',
    'mel': 'Melanoma (mel)',
    'vasc': 'Lesión vascular (vasc)'
}

# Instancio el explicador LIME una sola vez para reutilizarlo en cada petición
explainer_lime = lime_image.LimeImageExplainer()

def get_gradcam_heatmap(img_input, meta_input, model, last_conv_layer_name, pred_index):
    """
    Calcula el mapa de calor Grad-CAM, lo superpone a la imagen original 
    y lo devuelve codificado en Base64.
    """

    # Extraigo la parte convolucional del modelo para obtener los gradientes
    v_model = model.get_layer('coatnet0')
    inner_model = tf.keras.Model(
        inputs=v_model.inputs, 
        outputs=[v_model.get_layer(last_conv_layer_name).output, v_model.output]
    )
    pool_layer = [l for l in model.layers if isinstance(l, tf.keras.layers.GlobalAveragePooling2D)][0]
    concat_layer = [l for l in model.layers if isinstance(l, tf.keras.layers.Concatenate)][0]
    meta_branch = tf.keras.Model(inputs=model.input[1], outputs=concat_layer.input[1])
    
    # Construyo la parte superior del modelo (desde la concatenación hasta la salida) para poder calcular los gradientes correctamente
    top_input = tf.keras.Input(shape=concat_layer.output.shape[1:])
    x = top_input
    idx = model.layers.index(concat_layer)
    for layer in model.layers[idx+1:]:
        x = layer(x)
    top_model = tf.keras.Model(inputs=top_input, outputs=x)

    # Calculo los gradientes de la clase predicha respecto a la salida de la última capa convolucional
    with tf.GradientTape() as tape:
        conv_output, backbone_out = inner_model(img_input)
        x_img = pool_layer(backbone_out)
        x_meta = meta_branch(meta_input)
        combined_features = concat_layer([x_img, x_meta])
        predictions = top_model(combined_features)
        class_channel = predictions[:, pred_index]

    # Calculo el mapa de calor Grad-CAM
    grads = tape.gradient(class_channel, conv_output)
    pooled_grads = tf.reduce_mean(grads, axis=(0, 1, 2))
    heatmap = conv_output[0] @ pooled_grads[..., tf.newaxis]
    heatmap = tf.squeeze(heatmap)
    heatmap = tf.maximum(heatmap, 0) / (tf.math.reduce_max(heatmap) + 1e-10)

    # --- SUPERPOSICION MAPA DE CALOR A LA IMAGEN ---
    heatmap_uint8 = np.uint8(255 * heatmap)
    
    # Uso paleta 'jet' clásica (rojo = muy importante, azul = poco)
    jet = cm.get_cmap("jet")
    jet_colors = jet(np.arange(256))[:, :3]
    jet_heatmap = jet_colors[heatmap_uint8]
    
    # Redimensiono el mapa para que encaje con la imagen original
    jet_heatmap = tf.keras.utils.array_to_img(jet_heatmap)
    jet_heatmap = jet_heatmap.resize((224, 224))
    jet_heatmap = tf.keras.utils.img_to_array(jet_heatmap)
    
    # FusionO ambas imágenes (ajustar el 0.4 si se quiere el mapa más o menos opaco)
    original_img_array = tf.keras.utils.img_to_array(tf.keras.utils.array_to_img(img_input[0]))
    superimposed_img = jet_heatmap * 0.4 + original_img_array
    superimposed_img = tf.keras.utils.array_to_img(superimposed_img)
    
    # Codifico la imagen resultante a Base64 para enviarla en el JSON
    buffered = io.BytesIO()
    superimposed_img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    
    return img_str


@app.post("/predict")
async def predict(
    image: UploadFile = File(...),
    age: float = Form(...),
    sex: str = Form(...),
    localization: str = Form(...)
):
    # Proceso la imagen tal cual la espera el modelo
    contents = await image.read()
    original_pil_img = Image.open(io.BytesIO(contents)).convert("RGB")
    img_resized = original_pil_img.resize((224, 224))

    img_array = np.array(img_resized, dtype=np.float32) / 255.0
    img_array = np.expand_dims(img_array, axis=0) 

    # Preparo los metadatos exactamente igual que en el entrenamiento
    age_scaled = scaler.transform([[age]])
    cat_encoded = encoder.transform([[sex, localization]])
    meta_array = np.hstack([age_scaled, cat_encoded]).astype(np.float32)

    # Inferencia usando imagen y metadatos
    scores = model.predict([img_array, meta_array])[0]
    scores_dict = {translations[cls]: float(score) for cls, score in zip(classes, scores)}
    predicted_class = classes[np.argmax(scores)]
    confidence = float(np.max(scores))
    
    # 1. Grad-CAM. Genero el mapa de calor Grad-CAM y lo codifico en Base64 para enviarlo en el JSON
    gradcam_base64 = get_gradcam_heatmap(
        img_input=img_array,
        meta_input=meta_array,
        model=model,
        last_conv_layer_name=LAST_CONV_LAYER_NAME,
        pred_index=np.argmax(scores)
    )

    # WRAPPER PARA LIME/SHAP
    def hybrid_predict(batch):
        m_batch = np.repeat(meta_array, batch.shape[0], axis=0)
        return model.predict([batch, m_batch], verbose=0)

    # 2. LIME. Genero la explicación LIME y la codifico en Base64 para enviarla en el JSON
    exp = explainer_lime.explain_instance(
        img_array[0].astype(np.double),
        hybrid_predict, 
        top_labels=1, 
        num_samples=500,
        segmentation_fn=lambda x: quickshift(x, kernel_size=3, max_dist=6, ratio=0.5)
        #segmentation_fn=lambda x: slic(x, n_segments=250, compactness=10, sigma=1, start_label=1)
        #segmentation_fn=lambda x: felzenszwalb(x, scale=100, sigma=0.5, min_size=50)
        #segmentation_fn=lambda x: watershed(sobel(rgb2gray(x)), markers=250, compactness=0.001)
    )
    temp, mask = exp.get_image_and_mask(exp.top_labels[0], positive_only=True, num_features=5, hide_rest=False)
    lime_image = mark_boundaries(temp, mask)
    lime_pil = Image.fromarray((lime_image * 255).astype(np.uint8))
    buffered = io.BytesIO()
    lime_pil.save(buffered, format="JPEG")
    lime_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")


    return {
        "scores": scores_dict,
        "prediction": predicted_class,
        "confidence": confidence,
        "gradcam_image_base64": gradcam_base64,
        "lime_image_base64": lime_base64
    }