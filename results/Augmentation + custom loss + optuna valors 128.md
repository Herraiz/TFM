

# Modelo CoAtNet0 - Estudio: Augmentation + custom loss + optuna valors 128

============================================================
RENDIMIENTO GLOBAL
   - Accuracy Entrenamiento: 0.8139
   - Accuracy Validación:    0.7725
   - Accuracy Test:          0.7616
============================================================

## 📋 REPORTE DETALLADO POR CLASE (SET DE TEST):
                       precision    recall  f1-score   support

  Queratosis actínica       0.58      0.60      0.59        48
Carcinoma basocelular       0.61      0.55      0.58        66
   Queratosis benigna       0.70      0.52      0.60       172
       Dermatofibroma       0.12      0.60      0.20        10
   Nevus melanocítico       0.94      0.83      0.88      1016
             Melanoma       0.43      0.69      0.53       186
      Lesión vascular       0.74      0.90      0.81        29

             accuracy                           0.76      1527
            macro avg       0.59      0.67      0.60      1527
         weighted avg       0.81      0.76      0.78      1527


## 📋 REPORTE DETALLADO POR CLASE (SET DE VALIDACIÓN):
                       precision    recall  f1-score   support

  Queratosis actínica       0.61      0.63      0.62        57
Carcinoma basocelular       0.85      0.58      0.69        99
   Queratosis benigna       0.68      0.48      0.57       157
       Dermatofibroma       0.16      0.62      0.25        13
   Nevus melanocítico       0.93      0.87      0.90      1024
             Melanoma       0.37      0.61      0.46       156
      Lesión vascular       0.71      0.79      0.75        19

             accuracy                           0.77      1525
            macro avg       0.62      0.65      0.60      1525
         weighted avg       0.82      0.77      0.79      1525


## 📋 REPORTE DETALLADO POR CLASE (SET DE ENTRENAMIENTO):
                       precision    recall  f1-score   support

  Queratosis actínica       0.65      0.55      0.60       222
Carcinoma basocelular       0.81      0.72      0.76       349
   Queratosis benigna       0.77      0.58      0.66       770
       Dermatofibroma       0.36      0.92      0.52        92
   Nevus melanocítico       0.95      0.88      0.91      4665
             Melanoma       0.47      0.74      0.57       771
      Lesión vascular       0.80      0.98      0.88        94

             accuracy                           0.81      6963
            macro avg       0.69      0.77      0.70      6963
         weighted avg       0.85      0.81      0.82      6963

