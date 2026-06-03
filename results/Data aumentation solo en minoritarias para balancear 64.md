

# Modelo CoAtNet0 - Estudio: Data aumentation solo en minoritarias para balancear 64

============================================================
RENDIMIENTO GLOBAL
   - Accuracy Entrenamiento: 0.6991
   - Accuracy Validación:    0.6774
   - Accuracy Test:          0.6673
============================================================

## 📋 REPORTE DETALLADO POR CLASE (SET DE TEST):
                       precision    recall  f1-score   support

  Queratosis actínica       0.67      0.08      0.15        48
Carcinoma basocelular       0.68      0.26      0.37        66
   Queratosis benigna       0.39      0.09      0.15       172
       Dermatofibroma       0.00      0.00      0.00        10
   Nevus melanocítico       0.70      0.93      0.80      1016
             Melanoma       0.30      0.15      0.19       186
      Lesión vascular       0.75      0.21      0.32        29

             accuracy                           0.67      1527
            macro avg       0.50      0.25      0.28      1527
         weighted avg       0.61      0.67      0.60      1527


## 📋 REPORTE DETALLADO POR CLASE (SET DE VALIDACIÓN):
                       precision    recall  f1-score   support

  Queratosis actínica       0.70      0.12      0.21        57
Carcinoma basocelular       0.95      0.20      0.33        99
   Queratosis benigna       0.29      0.08      0.12       157
       Dermatofibroma       0.33      0.08      0.12        13
   Nevus melanocítico       0.71      0.94      0.81      1024
             Melanoma       0.23      0.11      0.15       156
      Lesión vascular       1.00      0.53      0.69        19

             accuracy                           0.68      1525
            macro avg       0.60      0.29      0.35      1525
         weighted avg       0.63      0.68      0.61      1525


## 📋 REPORTE DETALLADO POR CLASE (SET DE ENTRENAMIENTO):
                       precision    recall  f1-score   support

  Queratosis actínica       0.96      0.11      0.19       222
Carcinoma basocelular       0.93      0.39      0.55       349
   Queratosis benigna       0.53      0.12      0.20       770
       Dermatofibroma       0.57      0.40      0.47        92
   Nevus melanocítico       0.72      0.95      0.82      4665
             Melanoma       0.29      0.11      0.16       771
      Lesión vascular       0.99      0.71      0.83        94

             accuracy                           0.70      6963
            macro avg       0.71      0.40      0.46      6963
         weighted avg       0.67      0.70      0.64      6963

