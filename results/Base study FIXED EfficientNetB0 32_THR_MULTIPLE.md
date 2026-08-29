
# Modelo EfficientNetB0 - Estudio: Base study FIXED EfficientNetB0 32 (Sensibilidad Ajustada)

============================================================
CONFIGURACIÓN DE UMBRALES:
   - Melanoma: 0.1
   - Carcinoma Basocelular: Default
   - Queratosis Actínica: Default

RENDIMIENTO GLOBAL (Ajuste de Sensibilidad)
   - Accuracy Test:          0.18
============================================================

## 📋 REPORTE DETALLADO POR CLASE (SET DE TEST):
                       precision    recall  f1-score   support

  Queratosis actínica       0.06      0.56      0.11        48
Carcinoma basocelular       0.00      0.00      0.00        66
   Queratosis benigna       0.00      0.00      0.00       172
       Dermatofibroma       0.01      0.70      0.02        10
   Nevus melanocítico       0.94      0.20      0.32      1016
             Melanoma       0.25      0.26      0.25       186
      Lesión vascular       0.00      0.00      0.00        29

             accuracy                           0.18      1527
            macro avg       0.18      0.25      0.10      1527
         weighted avg       0.66      0.18      0.25      1527

