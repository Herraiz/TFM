
# Modelo EfficientNetB0 - Estudio: Base study FIXED and full traineable with 255 division EfficientNetB0 32 (Sensibilidad Ajustada)

============================================================
CONFIGURACIÓN DE UMBRALES:
   - Melanoma: 0.1
   - Carcinoma Basocelular: Default
   - Queratosis Actínica: Default

RENDIMIENTO GLOBAL (Ajuste de Sensibilidad)
   - Accuracy Test:          0.57
============================================================

## 📋 REPORTE DETALLADO POR CLASE (SET DE TEST):
                       precision    recall  f1-score   support

  Queratosis actínica       0.00      0.00      0.00        48
Carcinoma basocelular       0.00      0.00      0.00        66
   Queratosis benigna       0.31      0.75      0.43       172
       Dermatofibroma       0.02      0.30      0.04        10
   Nevus melanocítico       0.83      0.71      0.76      1016
             Melanoma       0.18      0.09      0.12       186
      Lesión vascular       0.00      0.00      0.00        29

             accuracy                           0.57      1527
            macro avg       0.19      0.26      0.19      1527
         weighted avg       0.61      0.57      0.57      1527

