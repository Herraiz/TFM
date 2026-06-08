"""
Utilidades de preprocesamiento de imagen y metadatos.
"""

import numpy as np
from PIL import Image

from config import IMAGE_SIZE


def preprocess_image(pil_image: Image.Image) -> np.ndarray:
    """
    Redimensiona y normaliza una imagen PIL a un array listo para el modelo.

    Returns:
        Array de forma (1, H, W, 3) con valores en [0, 1].
    """
    img_resized = pil_image.resize(IMAGE_SIZE)
    img_array = np.array(img_resized, dtype=np.float32) / 255.0
    return np.expand_dims(img_array, axis=0)


def preprocess_metadata(age: float, sex: str, localization: str, scaler, encoder) -> np.ndarray:
    """
    Escala la edad y codifica las variables categóricas exactamente
    igual que durante el entrenamiento.

    Returns:
        Array de forma (1, n_features) con dtype float32.
    """
    age_scaled = scaler.transform([[age]])
    cat_encoded = encoder.transform([[sex, localization]])
    return np.hstack([age_scaled, cat_encoded]).astype(np.float32)
