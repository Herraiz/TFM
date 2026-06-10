
# Modelo CoAtNet0 - Estudio: Augmentation + custom loss + optuna valors 128 (Sensibilidad Ajustada)

============================================================
CONFIGURACIÓN DE UMBRALES:
   - Melanoma: 0.23
   - Carcinoma Basocelular: Default
   - Queratosis Actínica: Default

RENDIMIENTO GLOBAL (Ajuste de Sensibilidad)
   - Accuracy Test:          0.63
============================================================

## 📋 REPORTE DETALLADO POR CLASE (SET DE TEST):
                       precision    recall  f1-score   support

  Queratosis actínica       0.57      0.52      0.54        48
Carcinoma basocelular       0.60      0.53      0.56        66
   Queratosis benigna       0.73      0.31      0.44       172
       Dermatofibroma       0.09      0.40      0.15        10
   Nevus melanocítico       0.97      0.64      0.77      1016
             Melanoma       0.28      0.90      0.42       186
      Lesión vascular       0.74      0.90      0.81        29

             accuracy                           0.63      1527
            macro avg       0.57      0.60      0.53      1527
         weighted avg       0.82      0.63      0.67      1527

