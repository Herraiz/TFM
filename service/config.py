"""
Constantes y configuración global de la aplicación.
"""

MODEL_PATH = "../models/implementation_best_1.keras"
SCALER_PATH = "../models/scaler.pkl"
ENCODER_PATH = "../models/encoder.pkl"

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
LIME_NUM_SAMPLES = 500 # Número de muestras sintéticas para LIME. Más muestras pueden mejorar la explicación, pero también aumentan el tiempo de cómputo.
LIME_NUM_FEATURES = 5 # Número de superpíxeles a mostrar en la explicación de LIME. Ajustar según el nivel de detalle deseado.
LIME_QUICKSHIFT_KERNEL_SIZE = 3 # Tamaño del kernel para segmentar la imagen en superpíxeles con el método quickshift de LIME. Un valor más alto genera superpíxeles más grandes, mientras que un valor más bajo genera superpíxeles más pequeños.
LIME_QUICKSHIFT_MAX_DIST = 6 # Distancia máxima para segmentar superpíxeles con el método quickshift de LIME. Un valor más alto puede generar superpíxeles más grandes, mientras que un valor más bajo puede generar superpíxeles más pequeños.
LIME_QUICKSHIFT_RATIO = 0.5 # Relación entre color y espacio para segmentar superpíxeles con el método quickshift de LIME. Un valor más alto da más peso al color, mientras que un valor más bajo da más peso al espacio.

# Parámetros de SHAP
SHAP_MAX_EVALS = 200 # Más valor implica mayor precisión en el mapa de calor, pero también más tiempo de cómputo y memoria.
SHAP_BATCH_SIZE = 124 # Tamaño de batch para SHAP. Ajustar según la memoria disponible. Un valor más alto puede acelerar el proceso, pero también aumentar el uso de memoria.
SHAP_BLUR_KERNEL = "blur(8,8)" # Tamaño del kernel de desenfoque para SHAP. Puede ser "gaussian", "median", "blur" o "box". El número entre paréntesis indica el tamaño del kernel. Ajustar según el nivel de ruido en las imágenes.
