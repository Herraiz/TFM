

# Modelo CoAtNet0 - Estudio: Augmentation + custom loss + optuna valors 64

============================================================
RENDIMIENTO GLOBAL
   - Accuracy Entrenamiento: 0.8581
   - Accuracy Validación:    0.7600
   - Accuracy Test:          0.7728
============================================================

## 📋 REPORTE DETALLADO POR CLASE (SET DE TEST):
                       precision    recall  f1-score   support

  Queratosis actínica       0.44      0.50      0.47        48
Carcinoma basocelular       0.84      0.58      0.68        66
   Queratosis benigna       0.65      0.56      0.60       172
       Dermatofibroma       0.17      0.20      0.18        10
   Nevus melanocítico       0.95      0.84      0.89      1016
             Melanoma       0.42      0.77      0.55       186
      Lesión vascular       0.88      0.76      0.81        29

             accuracy                           0.77      1527
            macro avg       0.62      0.60      0.60      1527
         weighted avg       0.82      0.77      0.79      1527


## 📋 REPORTE DETALLADO POR CLASE (SET DE VALIDACIÓN):
                       precision    recall  f1-score   support

  Queratosis actínica       0.54      0.70      0.61        57
Carcinoma basocelular       0.92      0.55      0.68        99
   Queratosis benigna       0.63      0.55      0.59       157
       Dermatofibroma       0.54      0.54      0.54        13
   Nevus melanocítico       0.93      0.84      0.89      1024
             Melanoma       0.32      0.62      0.42       156
      Lesión vascular       0.83      0.53      0.65        19

             accuracy                           0.76      1525
            macro avg       0.67      0.62      0.62      1525
         weighted avg       0.82      0.76      0.78      1525


## 📋 REPORTE DETALLADO POR CLASE (SET DE ENTRENAMIENTO):
                       precision    recall  f1-score   support

  Queratosis actínica       0.77      0.80      0.78       222
Carcinoma basocelular       0.93      0.74      0.82       349
   Queratosis benigna       0.85      0.71      0.77       770
       Dermatofibroma       0.69      0.92      0.79        92
   Nevus melanocítico       0.96      0.89      0.93      4665
             Melanoma       0.51      0.86      0.64       771
      Lesión vascular       0.99      0.93      0.96        94

             accuracy                           0.86      6963
            macro avg       0.82      0.83      0.81      6963
         weighted avg       0.89      0.86      0.87      6963

