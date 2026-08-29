
# Modelo EfficientNetB0 - Estudio: Base study FIXED with only fine-tuning EfficientNetB0 32 (Sensibilidad Ajustada)

============================================================
CONFIGURACIÓN DE UMBRALES:
   - Melanoma: 0.1
   - Carcinoma Basocelular: Default
   - Queratosis Actínica: Default

RENDIMIENTO GLOBAL (Ajuste de Sensibilidad)
   - Accuracy Test:          0.67
============================================================

## 📋 REPORTE DETALLADO POR CLASE (SET DE TEST):
                       precision    recall  f1-score   support

  Queratosis actínica       0.00      0.00      0.00        48
Carcinoma basocelular       0.00      0.00      0.00        66
   Queratosis benigna       0.00      0.00      0.00       172
       Dermatofibroma       0.00      0.00      0.00        10
   Nevus melanocítico       0.67      1.00      0.80      1016
             Melanoma       0.00      0.00      0.00       186
      Lesión vascular       0.00      0.00      0.00        29

             accuracy                           0.67      1527
            macro avg       0.10      0.14      0.11      1527
         weighted avg       0.44      0.67      0.53      1527

