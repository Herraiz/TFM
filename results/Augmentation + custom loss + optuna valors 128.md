

# Modelo CoAtNet0 - Estudio: Augmentation + custom loss + optuna valors 128

============================================================
RENDIMIENTO GLOBAL
   - Accuracy Entrenamiento: 0.9089
   - Accuracy Validación:    0.8236
   - Accuracy Test:          0.8271
============================================================

## 📋 REPORTE DETALLADO POR CLASE (SET DE TEST):
                       precision    recall  f1-score   support

  Queratosis actínica       0.78      0.38      0.51        48
Carcinoma basocelular       0.84      0.58      0.68        66
   Queratosis benigna       0.63      0.73      0.68       172
       Dermatofibroma       0.25      0.20      0.22        10
   Nevus melanocítico       0.89      0.95      0.92      1016
             Melanoma       0.63      0.48      0.55       186
      Lesión vascular       0.96      0.76      0.85        29

             accuracy                           0.83      1527
            macro avg       0.71      0.58      0.63      1527
         weighted avg       0.82      0.83      0.82      1527


## 📋 REPORTE DETALLADO POR CLASE (SET DE VALIDACIÓN):
                       precision    recall  f1-score   support

  Queratosis actínica       0.67      0.54      0.60        57
Carcinoma basocelular       0.96      0.46      0.63        99
   Queratosis benigna       0.60      0.71      0.65       157
       Dermatofibroma       0.50      0.23      0.32        13
   Nevus melanocítico       0.89      0.96      0.92      1024
             Melanoma       0.57      0.47      0.52       156
      Lesión vascular       0.80      0.63      0.71        19

             accuracy                           0.82      1525
            macro avg       0.71      0.57      0.62      1525
         weighted avg       0.82      0.82      0.81      1525


## 📋 REPORTE DETALLADO POR CLASE (SET DE ENTRENAMIENTO):
                       precision    recall  f1-score   support

  Queratosis actínica       0.93      0.64      0.76       222
Carcinoma basocelular       0.98      0.79      0.87       349
   Queratosis benigna       0.80      0.85      0.82       770
       Dermatofibroma       0.94      0.96      0.95        92
   Nevus melanocítico       0.93      0.99      0.96      4665
             Melanoma       0.84      0.62      0.71       771
      Lesión vascular       0.99      1.00      0.99        94

             accuracy                           0.91      6963
            macro avg       0.92      0.83      0.87      6963
         weighted avg       0.91      0.91      0.90      6963

