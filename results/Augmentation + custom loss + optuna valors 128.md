

# Modelo CoAtNet0 - Estudio: Augmentation + custom loss + optuna valors 128

============================================================
RENDIMIENTO GLOBAL
   - Accuracy Entrenamiento: 0.9012
   - Accuracy Validación:    0.8216
   - Accuracy Test:          0.8232
============================================================

## 📋 REPORTE DETALLADO POR CLASE (SET DE TEST):
                       precision    recall  f1-score   support

  Queratosis actínica       0.73      0.46      0.56        48
Carcinoma basocelular       0.92      0.52      0.66        66
   Queratosis benigna       0.61      0.80      0.69       172
       Dermatofibroma       0.50      0.20      0.29        10
   Nevus melanocítico       0.89      0.94      0.92      1016
             Melanoma       0.63      0.44      0.52       186
      Lesión vascular       0.88      0.76      0.81        29

             accuracy                           0.82      1527
            macro avg       0.74      0.59      0.64      1527
         weighted avg       0.82      0.82      0.81      1527


## 📋 REPORTE DETALLADO POR CLASE (SET DE VALIDACIÓN):
                       precision    recall  f1-score   support

  Queratosis actínica       0.69      0.51      0.59        57
Carcinoma basocelular       0.96      0.47      0.64        99
   Queratosis benigna       0.56      0.72      0.63       157
       Dermatofibroma       0.67      0.46      0.55        13
   Nevus melanocítico       0.90      0.95      0.93      1024
             Melanoma       0.56      0.46      0.51       156
      Lesión vascular       0.93      0.68      0.79        19

             accuracy                           0.82      1525
            macro avg       0.75      0.61      0.66      1525
         weighted avg       0.83      0.82      0.82      1525


## 📋 REPORTE DETALLADO POR CLASE (SET DE ENTRENAMIENTO):
                       precision    recall  f1-score   support

  Queratosis actínica       0.90      0.61      0.73       222
Carcinoma basocelular       0.98      0.76      0.86       349
   Queratosis benigna       0.76      0.87      0.81       770
       Dermatofibroma       0.93      0.93      0.93        92
   Nevus melanocítico       0.93      0.98      0.95      4665
             Melanoma       0.81      0.58      0.68       771
      Lesión vascular       1.00      1.00      1.00        94

             accuracy                           0.90      6963
            macro avg       0.90      0.82      0.85      6963
         weighted avg       0.90      0.90      0.90      6963

