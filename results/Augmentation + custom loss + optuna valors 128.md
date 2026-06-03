

# Modelo CoAtNet0 - Estudio: Augmentation + custom loss + optuna valors 128

============================================================
RENDIMIENTO GLOBAL
   - Accuracy Entrenamiento: 0.8565
   - Accuracy Validación:    0.8085
   - Accuracy Test:          0.7898
============================================================

## 📋 REPORTE DETALLADO POR CLASE (SET DE TEST):
                       precision    recall  f1-score   support

  Queratosis actínica       0.48      0.58      0.53        48
Carcinoma basocelular       0.61      0.70      0.65        66
   Queratosis benigna       0.60      0.52      0.56       172
       Dermatofibroma       0.12      0.20      0.15        10
   Nevus melanocítico       0.91      0.90      0.90      1016
             Melanoma       0.52      0.55      0.53       186
      Lesión vascular       0.96      0.83      0.89        29

             accuracy                           0.79      1527
            macro avg       0.60      0.61      0.60      1527
         weighted avg       0.80      0.79      0.79      1527


## 📋 REPORTE DETALLADO POR CLASE (SET DE VALIDACIÓN):
                       precision    recall  f1-score   support

  Queratosis actínica       0.55      0.72      0.63        57
Carcinoma basocelular       0.83      0.72      0.77        99
   Queratosis benigna       0.60      0.51      0.55       157
       Dermatofibroma       0.47      0.62      0.53        13
   Nevus melanocítico       0.90      0.92      0.91      1024
             Melanoma       0.50      0.52      0.51       156
      Lesión vascular       0.92      0.63      0.75        19

             accuracy                           0.81      1525
            macro avg       0.68      0.66      0.66      1525
         weighted avg       0.81      0.81      0.81      1525


## 📋 REPORTE DETALLADO POR CLASE (SET DE ENTRENAMIENTO):
                       precision    recall  f1-score   support

  Queratosis actínica       0.65      0.76      0.70       222
Carcinoma basocelular       0.82      0.85      0.84       349
   Queratosis benigna       0.76      0.61      0.68       770
       Dermatofibroma       0.57      0.92      0.71        92
   Nevus melanocítico       0.92      0.94      0.93      4665
             Melanoma       0.64      0.59      0.61       771
      Lesión vascular       0.98      0.98      0.98        94

             accuracy                           0.86      6963
            macro avg       0.76      0.81      0.78      6963
         weighted avg       0.85      0.86      0.85      6963

