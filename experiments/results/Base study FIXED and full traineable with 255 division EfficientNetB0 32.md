

# Modelo EfficientNetB0 - Estudio: Base study FIXED and full traineable with 255 division EfficientNetB0 32

============================================================
RENDIMIENTO GLOBAL
   - Accuracy Entrenamiento: 0.5913
   - Accuracy Validación:    0.5895
   - Accuracy Test:          0.5894
============================================================

## 📋 REPORTE DETALLADO POR CLASE (SET DE TEST):
                       precision    recall  f1-score   support

  Queratosis actínica       0.00      0.00      0.00        48
Carcinoma basocelular       0.00      0.00      0.00        66
   Queratosis benigna       0.30      0.78      0.44       172
       Dermatofibroma       0.02      0.30      0.04        10
   Nevus melanocítico       0.82      0.75      0.79      1016
             Melanoma       0.00      0.00      0.00       186
      Lesión vascular       0.00      0.00      0.00        29

             accuracy                           0.59      1527
            macro avg       0.16      0.26      0.18      1527
         weighted avg       0.58      0.59      0.57      1527


## 📋 REPORTE DETALLADO POR CLASE (SET DE VALIDACIÓN):
                       precision    recall  f1-score   support

  Queratosis actínica       0.00      0.00      0.00        57
Carcinoma basocelular       0.33      0.03      0.06        99
   Queratosis benigna       0.24      0.66      0.36       157
       Dermatofibroma       0.01      0.15      0.03        13
   Nevus melanocítico       0.83      0.77      0.80      1024
             Melanoma       0.00      0.00      0.00       156
      Lesión vascular       0.00      0.00      0.00        19

             accuracy                           0.59      1525
            macro avg       0.20      0.23      0.18      1525
         weighted avg       0.60      0.59      0.58      1525


## 📋 REPORTE DETALLADO POR CLASE (SET DE ENTRENAMIENTO):
                       precision    recall  f1-score   support

  Queratosis actínica       0.00      0.00      0.00       222
Carcinoma basocelular       0.07      0.01      0.01       349
   Queratosis benigna       0.28      0.66      0.39       770
       Dermatofibroma       0.05      0.40      0.09        92
   Nevus melanocítico       0.81      0.77      0.79      4665
             Melanoma       0.00      0.00      0.00       771
      Lesión vascular       0.00      0.00      0.00        94

             accuracy                           0.59      6963
            macro avg       0.17      0.26      0.18      6963
         weighted avg       0.58      0.59      0.57      6963

