

# Modelo CoAtNet0 - Estudio: Mixed Precision - Batch Size 168

============================================================
RENDIMIENTO GLOBAL
   - Accuracy Entrenamiento: 0.7863
   - Accuracy Validación:    0.7121
   - Accuracy Test:          0.7086
============================================================

## 📋 REPORTE DETALLADO POR CLASE (SET DE TEST):
                       precision    recall  f1-score   support

  Queratosis actínica       0.82      0.29      0.43        48
Carcinoma basocelular       0.81      0.71      0.76        66
   Queratosis benigna       0.50      0.64      0.56       172
       Dermatofibroma       0.20      0.40      0.27        10
   Nevus melanocítico       0.97      0.72      0.83      1016
             Melanoma       0.36      0.84      0.50       186
      Lesión vascular       0.75      0.72      0.74        29

             accuracy                           0.71      1527
            macro avg       0.63      0.62      0.58      1527
         weighted avg       0.83      0.71      0.74      1527


## 📋 REPORTE DETALLADO POR CLASE (SET DE VALIDACIÓN):
                       precision    recall  f1-score   support

  Queratosis actínica       0.81      0.37      0.51        57
Carcinoma basocelular       0.89      0.60      0.72        99
   Queratosis benigna       0.47      0.64      0.54       157
       Dermatofibroma       0.41      0.85      0.55        13
   Nevus melanocítico       0.96      0.74      0.84      1024
             Melanoma       0.31      0.76      0.44       156
      Lesión vascular       0.71      0.79      0.75        19

             accuracy                           0.71      1525
            macro avg       0.65      0.68      0.62      1525
         weighted avg       0.83      0.71      0.74      1525


## 📋 REPORTE DETALLADO POR CLASE (SET DE ENTRENAMIENTO):
                       precision    recall  f1-score   support

  Queratosis actínica       0.98      0.50      0.66       222
Carcinoma basocelular       0.91      0.81      0.85       349
   Queratosis benigna       0.67      0.77      0.72       770
       Dermatofibroma       0.61      0.91      0.73        92
   Nevus melanocítico       0.98      0.77      0.87      4665
             Melanoma       0.41      0.91      0.56       771
      Lesión vascular       0.85      1.00      0.92        94

             accuracy                           0.79      6963
            macro avg       0.77      0.81      0.76      6963
         weighted avg       0.87      0.79      0.81      6963

