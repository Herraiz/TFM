from fastapi import FastAPI, UploadFile, File, Form
import tensorflow as tf
import numpy as np
from PIL import Image
import io
import joblib
import base64
import matplotlib.cm as cm
from keras_cv_attention_models import coatnet


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
    predicted_class = classes[np.argmax(scores)]
    confidence = float(np.max(scores))
    
    # Genero el mapa de calor Grad-CAM y lo codifico en Base64 para enviarlo en el JSON
    gradcam_base64 = get_gradcam_heatmap(
        img_input=img_array,
        meta_input=meta_array,
        model=model,
        last_conv_layer_name=LAST_CONV_LAYER_NAME,
        pred_index=np.argmax(scores)
    )
    
    return {
        "prediction": predicted_class,
        "confidence": confidence,
        "gradcam_image_base64": gradcam_base64
    }