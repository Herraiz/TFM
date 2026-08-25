"""
Constantes y configuración global de la aplicación.
"""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = PROJECT_ROOT / "prod" / "final_model.keras"
SCALER_PATH = PROJECT_ROOT / "models" / "scaler.pkl"
ENCODER_PATH = PROJECT_ROOT / "models" / "encoder.pkl"

IMAGE_SIZE = (224, 224)
GRADCAM_ALPHA = 0.4  # Opacidad del mapa de calor superpuesto

# Orden de clases: debe coincidir con el del notebook de entrenamiento
CLASSES = ["akiec", "bcc", "bkl", "df", "nv", "mel", "vasc"]

CLASS_TRANSLATIONS = {
    "akiec": "Queratosis actínica (akiec)",
    "bcc": "Carcinoma basocelular (bcc)",
    "bkl": "Queratosis benigna (bkl)",
    "df": "Dermatofibroma (df)",
    "nv": "Nevus melanocítico (nv)",
    "mel": "Melanoma (mel)",
    "vasc": "Lesión vascular (vasc)",
}

# Parámetros de LIME
LIME_NUM_SAMPLES = 500
LIME_NUM_FEATURES = 5
LIME_QUICKSHIFT_KERNEL_SIZE = 3
LIME_QUICKSHIFT_MAX_DIST = 6
LIME_QUICKSHIFT_RATIO = 0.5

# Parámetros de SHAP
SHAP_MAX_EVALS = 200
SHAP_BATCH_SIZE = 124
SHAP_BLUR_KERNEL = "blur(8,8)"
