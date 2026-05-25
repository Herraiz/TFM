

# Modelo CoAtNet0 - Estudio: Mixed Precision: Exprimir el Batch Size sin perder rendimiento

============================================================
RENDIMIENTO GLOBAL
   - Accuracy Entrenamiento: 0.8291
   - Accuracy Validación:    0.7475
   - Accuracy Test:          0.7308
============================================================

## 📋 REPORTE DETALLADO POR CLASE (SET DE TEST):
                       precision    recall  f1-score   support

  Queratosis actínica       0.54      0.46      0.49        48
Carcinoma basocelular       0.85      0.62      0.72        66
   Queratosis benigna       0.49      0.88      0.63       172
       Dermatofibroma       0.24      0.80      0.37        10
   Nevus melanocítico       0.96      0.74      0.84      1016
             Melanoma       0.41      0.62      0.49       186
      Lesión vascular       0.79      0.79      0.79        29

             accuracy                           0.73      1527
            macro avg       0.61      0.70      0.62      1527
         weighted avg       0.81      0.73      0.75      1527


## 📋 REPORTE DETALLADO POR CLASE (SET DE VALIDACIÓN):
                       precision    recall  f1-score   support

  Queratosis actínica       0.69      0.67      0.68        57
Carcinoma basocelular       0.92      0.60      0.72        99
   Queratosis benigna       0.44      0.82      0.57       157
       Dermatofibroma       0.34      0.77      0.48        13
   Nevus melanocítico       0.96      0.78      0.86      1024
             Melanoma       0.38      0.58      0.46       156
      Lesión vascular       0.82      0.95      0.88        19

             accuracy                           0.75      1525
            macro avg       0.65      0.74      0.66      1525
         weighted avg       0.83      0.75      0.77      1525


## 📋 REPORTE DETALLADO POR CLASE (SET DE ENTRENAMIENTO):
                       precision    recall  f1-score   support

  Queratosis actínica       0.89      0.86      0.88       222
Carcinoma basocelular       0.93      0.85      0.89       349
   Queratosis benigna       0.62      0.93      0.75       770
       Dermatofibroma       0.55      0.98      0.71        92
   Nevus melanocítico       0.99      0.80      0.89      4665
             Melanoma       0.52      0.82      0.64       771
      Lesión vascular       0.93      1.00      0.96        94

             accuracy                           0.83      6963
            macro avg       0.78      0.89      0.82      6963
         weighted avg       0.88      0.83      0.84      6963

