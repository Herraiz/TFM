
# Modelo CoAtNet0 - Estudio: Augmentation + custom loss + optuna valors 128 (Sensibilidad Ajustada)

============================================================
CONFIGURACIÓN DE UMBRALES:
   - Melanoma: 0.28
   - Carcinoma Basocelular: Default
   - Queratosis Actínica: Default

RENDIMIENTO GLOBAL (Ajuste de Sensibilidad)
   - Accuracy Test:          0.71
============================================================

## 📋 REPORTE DETALLADO POR CLASE (SET DE TEST):
                       precision    recall  f1-score   support

  Queratosis actínica       0.48      0.58      0.53        48
Carcinoma basocelular       0.61      0.68      0.64        66
   Queratosis benigna       0.61      0.47      0.53       172
       Dermatofibroma       0.12      0.20      0.15        10
   Nevus melanocítico       0.95      0.74      0.83      1016
             Melanoma       0.34      0.78      0.47       186
      Lesión vascular       0.96      0.83      0.89        29

             accuracy                           0.71      1527
            macro avg       0.58      0.61      0.58      1527
         weighted avg       0.80      0.71      0.73      1527

