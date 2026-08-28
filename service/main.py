"""
API REST para clasificación de lesiones cutáneas con explicabilidad.

Endpoints:
    POST /predict - Devuelve la predicción y los mapas Grad-CAM, LIME y SHAP.
"""

import io
import os
os.environ["TF_USE_LEGACY_KERAS"] = "1"
from time import time
from fastapi import FastAPI, File, Form, UploadFile
from PIL import Image
from pydantic import BaseModel
from typing import Dict
from service.config_chuc import CLASS_TRANSLATIONS
from service.explainability_chuc import get_gradcam, get_lime, get_shap
from service.preprocessing import preprocess_image, preprocess_metadata
from service.model_chuc import (
    get_last_conv_layer_name,
    load_model,
    load_preprocessors,
    make_hybrid_predict_fn,
    run_inference,
)
import tensorflow as tf
from fastapi.middleware.cors import CORSMiddleware


# ---------------------------------------------------------------------------
# Inicio de la aplicación y carga de artefactos
# ---------------------------------------------------------------------------

# Limpiamos primero la sesión de TensorFlow para evitar conflictos con modelos anteriores

tf.keras.backend.clear_session()

app = FastAPI(title="Skin Lesion Classifier")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://chuc1skynet.huc.es:8999"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
class PredictionResponse(BaseModel):
    prediction: str
    prediction_score: float
    scores: Dict[str, float]
    gradcam_image_base64: str
    lime_image_base64: str
    shap_image_base64: str
    shap_min: float = None
    shap_max: float = None


@app.post("/predict", response_model=PredictionResponse)
@app.post("/api/predict", response_model=PredictionResponse, include_in_schema=False)
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
    gradcam_base64 = get_gradcam(img_array, meta_array, model, LAST_CONV_LAYER_NAME, pred_index)
    lime_base64 = get_lime(img_array, predict_fn)
    shap_base64, (shap_min, shap_max) = get_shap(img_array, predict_fn, pred_index)

    print("#" * 50)

    response = PredictionResponse(
        prediction=CLASS_TRANSLATIONS[result["predicted_class"]],
        prediction_score=result["confidence"],
        scores=result["scores"],
        gradcam_image_base64=gradcam_base64,
        lime_image_base64=lime_base64,
        shap_image_base64=shap_base64,
        shap_min=shap_min,
        shap_max=shap_max,
    )

    print(response.prediction, f"({response.prediction_score:.2f}),", f"Scores: {response.scores}")
    print(f"Tiempo de procesamiento: {time() - start_time:.2f}s")

    return response
