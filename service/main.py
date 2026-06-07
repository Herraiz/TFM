from fastapi import FastAPI, UploadFile, File, Form
import tensorflow as tf
import numpy as np
from PIL import Image
import io
import joblib  # Necesario para cargar los preprocesadores
from sklearn.preprocessing import StandardScaler, OneHotEncoder

app = FastAPI()

# 1. Cargar el modelo guardado
model = tf.saved_model.load("../models/baseline2/v1")
infer = model.signatures["serving_default"]

print("------------------------------")
print("Firmas del modelo:", infer.structured_input_signature)
print("------------------------------")


# 2. Cargar los objetos de preprocesamiento entrenados
try:
    scaler = joblib.load("../models/scaler.pkl")
    encoder = joblib.load("../models/encoder.pkl")
except FileNotFoundError:
    print("⚠️ Recuerda generar y guardar scaler.pkl y encoder.pkl desde tu notebook.")


classes = [
    "akiec",
    "bcc",
    "bkl",
    "df",
    "nv",
    "mel",
    "vasc"
]

@app.post("/predict")
async def predict(
    image: UploadFile = File(...),
    age: float = Form(...),
    sex: str = Form(...),
    localization: str = Form(...)
):
    # --- TRATAMIENTO DE LA IMAGEN ---
    contents = await image.read()
    img = Image.open(io.BytesIO(contents)).convert("RGB")
    img = img.resize((224, 224))

    # Normalizamos y añadimos la dimensión del batch -> Shape final: (1, 224, 224, 3)
    img_array = np.array(img, dtype=np.float32) / 255.0
    img_array = np.expand_dims(img_array, axis=0) 

    # --- TRATAMIENTO DE LOS METADATOS ---
    # Es fundamental pasar las variables como listas de listas (matrices 2D) para los transform
    age_scaled = scaler.transform([[age]])
    cat_encoded = encoder.transform([[sex, localization]])

    # Ensamblamos el vector final exactamente como en el notebook
    meta_array = np.hstack([age_scaled, cat_encoded]).astype(np.float32)

    print("--------- meta_array ---------")
    print(meta_array)  # Imprime la salida completa para verificar la estructura
    print("------------------------------")

    # --- INFERENCIA ---
    # ¡OJO A ESTE DETALLE!: Los nombres de los parámetros (aquí puestos como 'image_input' e 'meta_input')
    # deben coincidir estrictamente con las claves que te imprima la consola en `infer.structured_input_signature`.
    # Los nombres se establencen al crear el modelo.
    prediction = infer(
        image_input=tf.constant(img_array),
        meta_input=tf.constant(meta_array)
    )
    
    print("------------------------------")
    print(prediction)  # Imprime la salida completa para verificar la estructura
    print("------------------------------")


    # Extraemos las predicciones. Hay que ajustar la clave a buscar según lo que te imprima la consola en `prediction`.
    scores = prediction["predictions_float32"].numpy()[0]

    print("Scores calculados:", scores)

    predicted_class = classes[np.argmax(scores)]
    confidence = float(np.max(scores))
    
    return {
        "prediction": predicted_class,
        "confidence": confidence
    }