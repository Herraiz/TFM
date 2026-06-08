"""
API REST para clasificación de lesiones cutáneas con explicabilidad.

Endpoints:
    POST /predict - Devuelve la predicción y los mapas Grad-CAM, LIME y SHAP.
"""

import io
from time import time

import numpy as np
from fastapi import FastAPI, File, Form, UploadFile
from PIL import Image

from config import CLASSES
from explainability import get_gradcam_base64, get_lime_base64, get_shap_base64
from model import (
    get_last_conv_layer_name,
    load_model,
    load_preprocessors,
    make_hybrid_predict_fn,
    run_inference,
)
from preprocessing import preprocess_image, preprocess_metadata

# ---------------------------------------------------------------------------
# Inicio de la aplicación y carga de artefactos
# ---------------------------------------------------------------------------

app = FastAPI(title="Skin Lesion Classifier")

scaler, encoder = load_preprocessors()
model = load_model()
LAST_CONV_LAYER_NAME = get_last_conv_layer_name(model)

print("#" * 50)
print(f"Última capa convolucional detectada: {LAST_CONV_LAYER_NAME}")
print(f"Clases del encoder: {encoder.get_feature_names_out()}")
print("#" * 50)


# ---------------------------------------------------------------------------
# Endpoint de predicción
# ---------------------------------------------------------------------------

@app.post("/predict")
async def predict(
    image: UploadFile = File(...),
    age: float = Form(...),
    sex: str = Form(...),
    localization: str = Form(...),
):
    start_time = time()

    # 1. Preprocesamiento
    contents = await image.read()
    pil_image = Image.open(io.BytesIO(contents)).convert("RGB")
    img_array = preprocess_image(pil_image)
    meta_array = preprocess_metadata(age, sex, localization, scaler, encoder)

    # 2. Inferencia
    result = run_inference(model, img_array, meta_array)
    pred_index = result["pred_index"]
    predict_fn = make_hybrid_predict_fn(model, meta_array)

    # 3. Explicabilidad
    gradcam_base64 = get_gradcam_base64(img_array, meta_array, model, LAST_CONV_LAYER_NAME, pred_index)
    lime_base64 = get_lime_base64(img_array, predict_fn)
    shap_base64 = get_shap_base64(img_array, predict_fn, pred_index)

    print(f"########### Tiempo de procesamiento: {time() - start_time:.2f}s")

    return {
        "scores": result["scores"],
        "prediction": result["predicted_class"],
        "confidence": result["confidence"],
        "gradcam_image_base64": gradcam_base64,
        "lime_image_base64": lime_base64,
        "shap_image_base64": shap_base64,
    }
