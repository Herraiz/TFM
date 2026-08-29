
# Modelo CoAtNet-0 - Estudio: CoatNet without metadata 32 (Sensibilidad Ajustada)

============================================================
CONFIGURACIÓN DE UMBRALES:
   - Melanoma: 0.15
   - Carcinoma Basocelular: Default
   - Queratosis Actínica: Default

RENDIMIENTO GLOBAL (Ajuste de Sensibilidad)
   - Accuracy Test:          0.59
============================================================

## 📋 REPORTE DETALLADO POR CLASE (SET DE TEST):
                       precision    recall  f1-score   support

  Queratosis actínica       0.50      0.40      0.44        48
Carcinoma basocelular       0.76      0.53      0.62        66
   Queratosis benigna       0.54      0.29      0.38       172
       Dermatofibroma       0.00      0.00      0.00        10
   Nevus melanocítico       0.97      0.60      0.74      1016
             Melanoma       0.25      0.94      0.39       186
      Lesión vascular       0.90      0.62      0.73        29

             accuracy                           0.59      1527
            macro avg       0.56      0.48      0.47      1527
         weighted avg       0.80      0.59      0.64      1527

