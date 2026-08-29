

# Modelo EfficientNetB0 - Estudio: Base study FIXED with only fine-tuning EfficientNetB0 32

============================================================
RENDIMIENTO GLOBAL
   - Accuracy Entrenamiento: 0.6700
   - Accuracy Validación:    0.6715
   - Accuracy Test:          0.6654
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


## 📋 REPORTE DETALLADO POR CLASE (SET DE VALIDACIÓN):
                       precision    recall  f1-score   support

  Queratosis actínica       0.00      0.00      0.00        57
Carcinoma basocelular       0.00      0.00      0.00        99
   Queratosis benigna       0.00      0.00      0.00       157
       Dermatofibroma       0.00      0.00      0.00        13
   Nevus melanocítico       0.67      1.00      0.80      1024
             Melanoma       0.00      0.00      0.00       156
      Lesión vascular       0.00      0.00      0.00        19

             accuracy                           0.67      1525
            macro avg       0.10      0.14      0.11      1525
         weighted avg       0.45      0.67      0.54      1525


## 📋 REPORTE DETALLADO POR CLASE (SET DE ENTRENAMIENTO):
                       precision    recall  f1-score   support

  Queratosis actínica       0.00      0.00      0.00       222
Carcinoma basocelular       0.00      0.00      0.00       349
   Queratosis benigna       0.00      0.00      0.00       770
       Dermatofibroma       0.00      0.00      0.00        92
   Nevus melanocítico       0.67      1.00      0.80      4665
             Melanoma       0.00      0.00      0.00       771
      Lesión vascular       0.00      0.00      0.00        94

             accuracy                           0.67      6963
            macro avg       0.10      0.14      0.11      6963
         weighted avg       0.45      0.67      0.54      6963

