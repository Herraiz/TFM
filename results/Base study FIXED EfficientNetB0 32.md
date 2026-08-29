

# Modelo EfficientNetB0 - Estudio: Base study FIXED EfficientNetB0 32

============================================================
RENDIMIENTO GLOBAL
   - Accuracy Entrenamiento: 0.1624
   - Accuracy Validación:    0.1725
   - Accuracy Test:          0.1578
============================================================

## 📋 REPORTE DETALLADO POR CLASE (SET DE TEST):
                       precision    recall  f1-score   support

  Queratosis actínica       0.06      0.73      0.11        48
Carcinoma basocelular       0.00      0.00      0.00        66
   Queratosis benigna       0.00      0.00      0.00       172
       Dermatofibroma       0.01      0.70      0.02        10
   Nevus melanocítico       0.94      0.20      0.32      1016
             Melanoma       0.00      0.00      0.00       186
      Lesión vascular       0.00      0.00      0.00        29

             accuracy                           0.16      1527
            macro avg       0.14      0.23      0.06      1527
         weighted avg       0.63      0.16      0.22      1527


## 📋 REPORTE DETALLADO POR CLASE (SET DE VALIDACIÓN):
                       precision    recall  f1-score   support

  Queratosis actínica       0.06      0.67      0.11        57
Carcinoma basocelular       0.15      0.03      0.05        99
   Queratosis benigna       0.00      0.00      0.00       157
       Dermatofibroma       0.01      0.62      0.02        13
   Nevus melanocítico       0.91      0.21      0.34      1024
             Melanoma       0.00      0.00      0.00       156
      Lesión vascular       0.00      0.00      0.00        19

             accuracy                           0.17      1525
            macro avg       0.16      0.22      0.08      1525
         weighted avg       0.63      0.17      0.24      1525


## 📋 REPORTE DETALLADO POR CLASE (SET DE ENTRENAMIENTO):
                       precision    recall  f1-score   support

  Queratosis actínica       0.06      0.69      0.10       222
Carcinoma basocelular       0.10      0.03      0.04       349
   Queratosis benigna       0.00      0.00      0.00       770
       Dermatofibroma       0.02      0.82      0.05        92
   Nevus melanocítico       0.92      0.19      0.32      4665
             Melanoma       0.00      0.00      0.00       771
      Lesión vascular       0.00      0.00      0.00        94

             accuracy                           0.16      6963
            macro avg       0.16      0.25      0.07      6963
         weighted avg       0.62      0.16      0.22      6963

