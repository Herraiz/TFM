
# Modelo CoAtNet0 - Estudio: Augmentation + custom loss + optuna valors 128 (Sensibilidad Ajustada)

============================================================
CONFIGURACIÓN DE UMBRALES:
   - Melanoma: 0.1
   - Carcinoma Basocelular: Default
   - Queratosis Actínica: Default

RENDIMIENTO GLOBAL (Ajuste de Sensibilidad)
   - Accuracy Test:          0.65
============================================================

## 📋 REPORTE DETALLADO POR CLASE (SET DE TEST):
                       precision    recall  f1-score   support

  Queratosis actínica       0.80      0.17      0.28        48
Carcinoma basocelular       0.62      0.80      0.70        66
   Queratosis benigna       0.71      0.37      0.48       172
       Dermatofibroma       1.00      0.20      0.33        10
   Nevus melanocítico       0.98      0.67      0.79      1016
             Melanoma       0.27      0.91      0.42       186
      Lesión vascular       0.96      0.83      0.89        29

             accuracy                           0.65      1527
            macro avg       0.76      0.56      0.56      1527
         weighted avg       0.84      0.65      0.69      1527

