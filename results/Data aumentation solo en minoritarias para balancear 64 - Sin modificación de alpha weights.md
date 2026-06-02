

# Modelo CoAtNet0 - Estudio: Data aumentation solo en minoritarias para balancear 64 - Sin modificación de alpha weights

============================================================
RENDIMIENTO GLOBAL
   - Accuracy Entrenamiento: 0.6876
   - Accuracy Validación:    0.6872
   - Accuracy Test:          0.6811
============================================================

## 📋 REPORTE DETALLADO POR CLASE (SET DE TEST):
                       precision    recall  f1-score   support

  Queratosis actínica       0.64      0.15      0.24        48
Carcinoma basocelular       0.89      0.12      0.21        66
   Queratosis benigna       0.36      0.08      0.13       172
       Dermatofibroma       0.00      0.00      0.00        10
   Nevus melanocítico       0.71      0.96      0.82      1016
             Melanoma       0.32      0.12      0.18       186
      Lesión vascular       0.87      0.45      0.59        29

             accuracy                           0.68      1527
            macro avg       0.54      0.27      0.31      1527
         weighted avg       0.63      0.68      0.61      1527


## 📋 REPORTE DETALLADO POR CLASE (SET DE VALIDACIÓN):
                       precision    recall  f1-score   support

  Queratosis actínica       0.67      0.14      0.23        57
Carcinoma basocelular       0.88      0.14      0.24        99
   Queratosis benigna       0.30      0.08      0.13       157
       Dermatofibroma       0.67      0.15      0.25        13
   Nevus melanocítico       0.71      0.96      0.82      1024
             Melanoma       0.27      0.08      0.13       156
      Lesión vascular       0.79      0.58      0.67        19

             accuracy                           0.69      1525
            macro avg       0.61      0.31      0.35      1525
         weighted avg       0.63      0.69      0.61      1525


## 📋 REPORTE DETALLADO POR CLASE (SET DE ENTRENAMIENTO):
                       precision    recall  f1-score   support

  Queratosis actínica       0.55      0.10      0.17       222
Carcinoma basocelular       0.81      0.19      0.31       349
   Queratosis benigna       0.44      0.11      0.17       770
       Dermatofibroma       0.48      0.23      0.31        92
   Nevus melanocítico       0.71      0.96      0.81      4665
             Melanoma       0.33      0.09      0.14       771
      Lesión vascular       0.90      0.60      0.72        94

             accuracy                           0.69      6963
            macro avg       0.60      0.32      0.38      6963
         weighted avg       0.63      0.69      0.61      6963

