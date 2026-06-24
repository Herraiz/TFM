

# Modelo CoAtNet3 - Estudio: Augmentation + custom loss + optuna valors 32

============================================================
RENDIMIENTO GLOBAL
   - Accuracy Entrenamiento: 0.7333
   - Accuracy Validación:    0.7298
   - Accuracy Test:          0.7276
============================================================

## 📋 REPORTE DETALLADO POR CLASE (SET DE TEST):
                       precision    recall  f1-score   support

  Queratosis actínica       0.25      0.12      0.17        48
Carcinoma basocelular       0.39      0.64      0.49        66
   Queratosis benigna       0.47      0.42      0.45       172
       Dermatofibroma       0.00      0.00      0.00        10
   Nevus melanocítico       0.81      0.94      0.87      1016
             Melanoma       0.48      0.16      0.24       186
      Lesión vascular       0.77      0.34      0.48        29

             accuracy                           0.73      1527
            macro avg       0.45      0.37      0.38      1527
         weighted avg       0.69      0.73      0.69      1527


## 📋 REPORTE DETALLADO POR CLASE (SET DE VALIDACIÓN):
                       precision    recall  f1-score   support

  Queratosis actínica       0.43      0.21      0.28        57
Carcinoma basocelular       0.43      0.53      0.47        99
   Queratosis benigna       0.41      0.41      0.41       157
       Dermatofibroma       0.50      0.08      0.13        13
   Nevus melanocítico       0.82      0.93      0.87      1024
             Melanoma       0.50      0.17      0.26       156
      Lesión vascular       0.80      0.42      0.55        19

             accuracy                           0.73      1525
            macro avg       0.56      0.39      0.43      1525
         weighted avg       0.70      0.73      0.70      1525


## 📋 REPORTE DETALLADO POR CLASE (SET DE ENTRENAMIENTO):
                       precision    recall  f1-score   support

  Queratosis actínica       0.25      0.13      0.17       222
Carcinoma basocelular       0.39      0.53      0.45       349
   Queratosis benigna       0.47      0.36      0.41       770
       Dermatofibroma       0.43      0.03      0.06        92
   Nevus melanocítico       0.81      0.95      0.87      4665
             Melanoma       0.55      0.15      0.23       771
      Lesión vascular       0.82      0.52      0.64        94

             accuracy                           0.73      6963
            macro avg       0.53      0.38      0.41      6963
         weighted avg       0.70      0.73      0.69      6963

