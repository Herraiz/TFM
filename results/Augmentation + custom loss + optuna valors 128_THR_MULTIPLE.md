
# Modelo CoAtNet0 - Estudio: Augmentation + custom loss + optuna valors 128 (Sensibilidad Ajustada)

============================================================
CONFIGURACIÓN DE UMBRALES:
   - Melanoma: 0.2
   - Carcinoma Basocelular: 0.2
   - Queratosis Actínica: 0.1

RENDIMIENTO GLOBAL (Ajuste de Sensibilidad)
   - Accuracy Test:          0.72
============================================================

## 📋 REPORTE DETALLADO POR CLASE (SET DE TEST):
                       precision    recall  f1-score   support

  Queratosis actínica       0.50      0.48      0.49        48
Carcinoma basocelular       0.62      0.74      0.68        66
   Queratosis benigna       0.65      0.44      0.52       172
       Dermatofibroma       0.33      0.50      0.40        10
   Nevus melanocítico       0.95      0.76      0.84      1016
             Melanoma       0.35      0.81      0.49       186
      Lesión vascular       0.73      0.83      0.77        29

             accuracy                           0.72      1527
            macro avg       0.59      0.65      0.60      1527
         weighted avg       0.80      0.72      0.74      1527

