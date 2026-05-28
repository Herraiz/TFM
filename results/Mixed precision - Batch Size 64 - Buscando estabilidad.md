

# Modelo CoAtNet0 - Estudio: Mixed precision - Batch Size 64 - Buscando estabilidad

============================================================
RENDIMIENTO GLOBAL
   - Accuracy Entrenamiento: 0.7390
   - Accuracy Validación:    0.6866
   - Accuracy Test:          0.6843
============================================================

## 📋 REPORTE DETALLADO POR CLASE (SET DE TEST):
                       precision    recall  f1-score   support

  Queratosis actínica       0.65      0.31      0.42        48
Carcinoma basocelular       0.80      0.65      0.72        66
   Queratosis benigna       0.55      0.69      0.61       172
       Dermatofibroma       0.22      0.50      0.30        10
   Nevus melanocítico       0.95      0.69      0.80      1016
             Melanoma       0.32      0.75      0.45       186
      Lesión vascular       0.66      0.86      0.75        29

             accuracy                           0.68      1527
            macro avg       0.59      0.64      0.58      1527
         weighted avg       0.80      0.68      0.72      1527


## 📋 REPORTE DETALLADO POR CLASE (SET DE VALIDACIÓN):
                       precision    recall  f1-score   support

  Queratosis actínica       0.80      0.42      0.55        57
Carcinoma basocelular       0.82      0.45      0.58        99
   Queratosis benigna       0.48      0.68      0.56       157
       Dermatofibroma       0.27      0.69      0.39        13
   Nevus melanocítico       0.96      0.72      0.82      1024
             Melanoma       0.29      0.73      0.41       156
      Lesión vascular       0.60      0.79      0.68        19

             accuracy                           0.69      1525
            macro avg       0.60      0.64      0.57      1525
         weighted avg       0.82      0.69      0.72      1525


## 📋 REPORTE DETALLADO POR CLASE (SET DE ENTRENAMIENTO):
                       precision    recall  f1-score   support

  Queratosis actínica       0.85      0.45      0.59       222
Carcinoma basocelular       0.88      0.64      0.74       349
   Queratosis benigna       0.62      0.73      0.67       770
       Dermatofibroma       0.45      0.89      0.60        92
   Nevus melanocítico       0.97      0.73      0.84      4665
             Melanoma       0.36      0.86      0.51       771
      Lesión vascular       0.73      1.00      0.85        94

             accuracy                           0.74      6963
            macro avg       0.69      0.76      0.68      6963
         weighted avg       0.85      0.74      0.77      6963

