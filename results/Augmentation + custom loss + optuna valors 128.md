

# Modelo CoAtNet0 - Estudio: Augmentation + custom loss + optuna valors 128

============================================================
RENDIMIENTO GLOBAL
   - Accuracy Entrenamiento: 0.9041
   - Accuracy Validación:    0.8210
   - Accuracy Test:          0.8225
============================================================

## 📋 REPORTE DETALLADO POR CLASE (SET DE TEST):
                       precision    recall  f1-score   support

  Queratosis actínica       0.76      0.27      0.40        48
Carcinoma basocelular       0.58      0.86      0.70        66
   Queratosis benigna       0.65      0.73      0.69       172
       Dermatofibroma       0.80      0.40      0.53        10
   Nevus melanocítico       0.90      0.93      0.92      1016
             Melanoma       0.60      0.45      0.51       186
      Lesión vascular       0.96      0.83      0.89        29

             accuracy                           0.82      1527
            macro avg       0.75      0.64      0.66      1527
         weighted avg       0.82      0.82      0.81      1527


## 📋 REPORTE DETALLADO POR CLASE (SET DE VALIDACIÓN):
                       precision    recall  f1-score   support

  Queratosis actínica       0.91      0.37      0.53        57
Carcinoma basocelular       0.69      0.78      0.73        99
   Queratosis benigna       0.59      0.69      0.64       157
       Dermatofibroma       0.73      0.62      0.67        13
   Nevus melanocítico       0.92      0.93      0.92      1024
             Melanoma       0.52      0.48      0.50       156
      Lesión vascular       0.86      0.63      0.73        19

             accuracy                           0.82      1525
            macro avg       0.74      0.64      0.67      1525
         weighted avg       0.82      0.82      0.82      1525


## 📋 REPORTE DETALLADO POR CLASE (SET DE ENTRENAMIENTO):
                       precision    recall  f1-score   support

  Queratosis actínica       0.95      0.49      0.64       222
Carcinoma basocelular       0.80      0.97      0.87       349
   Queratosis benigna       0.84      0.85      0.85       770
       Dermatofibroma       0.97      0.92      0.94        92
   Nevus melanocítico       0.94      0.97      0.95      4665
             Melanoma       0.76      0.63      0.69       771
      Lesión vascular       0.96      0.99      0.97        94

             accuracy                           0.90      6963
            macro avg       0.89      0.83      0.85      6963
         weighted avg       0.90      0.90      0.90      6963

