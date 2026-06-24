
# Modelo CoAtNet3 - Estudio: Augmentation + custom loss + optuna valors 32 (Sensibilidad Ajustada)

============================================================
CONFIGURACIÓN DE UMBRALES:
   - Melanoma: 0.1
   - Carcinoma Basocelular: Default
   - Queratosis Actínica: Default

RENDIMIENTO GLOBAL (Ajuste de Sensibilidad)
   - Accuracy Test:          0.44
============================================================

## 📋 REPORTE DETALLADO POR CLASE (SET DE TEST):
                       precision    recall  f1-score   support

  Queratosis actínica       0.29      0.04      0.07        48
Carcinoma basocelular       0.43      0.61      0.50        66
   Queratosis benigna       0.40      0.05      0.08       172
       Dermatofibroma       0.00      0.00      0.00        10
   Nevus melanocítico       0.97      0.43      0.60      1016
             Melanoma       0.19      0.94      0.31       186
      Lesión vascular       0.77      0.34      0.48        29

             accuracy                           0.44      1527
            macro avg       0.43      0.34      0.29      1527
         weighted avg       0.75      0.44      0.48      1527

