

# Modelo CoAtNet0 - Estudio: Augmentation + custom loss + optuna valors 128

============================================================
RENDIMIENTO GLOBAL
   - Accuracy Entrenamiento: 0.8396
   - Accuracy Validación:    0.8026
   - Accuracy Test:          0.7904
============================================================

## 📋 REPORTE DETALLADO POR CLASE (SET DE TEST):
                       precision    recall  f1-score   support

  Queratosis actínica       1.00      0.21      0.34        48
Carcinoma basocelular       0.76      0.68      0.72        66
   Queratosis benigna       0.55      0.75      0.63       172
       Dermatofibroma       0.37      0.70      0.48        10
   Nevus melanocítico       0.86      0.94      0.90      1016
             Melanoma       0.71      0.19      0.30       186
      Lesión vascular       0.71      0.83      0.76        29

             accuracy                           0.79      1527
            macro avg       0.71      0.61      0.59      1527
         weighted avg       0.80      0.79      0.76      1527


## 📋 REPORTE DETALLADO POR CLASE (SET DE VALIDACIÓN):
                       precision    recall  f1-score   support

  Queratosis actínica       0.76      0.28      0.41        57
Carcinoma basocelular       0.83      0.60      0.69        99
   Queratosis benigna       0.50      0.71      0.59       157
       Dermatofibroma       0.33      0.54      0.41        13
   Nevus melanocítico       0.88      0.96      0.92      1024
             Melanoma       0.65      0.21      0.32       156
      Lesión vascular       0.78      0.74      0.76        19

             accuracy                           0.80      1525
            macro avg       0.68      0.58      0.59      1525
         weighted avg       0.80      0.80      0.78      1525


## 📋 REPORTE DETALLADO POR CLASE (SET DE ENTRENAMIENTO):
                       precision    recall  f1-score   support

  Queratosis actínica       0.89      0.32      0.48       222
Carcinoma basocelular       0.90      0.83      0.86       349
   Queratosis benigna       0.62      0.75      0.68       770
       Dermatofibroma       0.56      0.91      0.69        92
   Nevus melanocítico       0.88      0.97      0.92      4665
             Melanoma       0.86      0.27      0.41       771
      Lesión vascular       0.81      0.97      0.88        94

             accuracy                           0.84      6963
            macro avg       0.79      0.72      0.70      6963
         weighted avg       0.85      0.84      0.82      6963

