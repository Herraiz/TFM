
# Modelo CoAtNet0 - Estudio: Augmentation + custom loss + optuna valors 128 (Sensibilidad Ajustada)

============================================================
CONFIGURACIÓN DE UMBRALES:
   - Melanoma: 0.1
   - Carcinoma Basocelular: Default
   - Queratosis Actínica: Default

RENDIMIENTO GLOBAL (Ajuste de Sensibilidad)
   - Accuracy Test:          0.58
============================================================

## 📋 REPORTE DETALLADO POR CLASE (SET DE TEST):
                       precision    recall  f1-score   support

  Queratosis actínica       0.38      0.38      0.38        48
Carcinoma basocelular       0.62      0.65      0.64        66
   Queratosis benigna       0.83      0.14      0.24       172
       Dermatofibroma       0.20      0.10      0.13        10
   Nevus melanocítico       0.97      0.60      0.74      1016
             Melanoma       0.23      0.90      0.37       186
      Lesión vascular       0.64      0.86      0.74        29

             accuracy                           0.58      1527
            macro avg       0.55      0.52      0.46      1527
         weighted avg       0.82      0.58      0.62      1527

