

# Modelo CoAtNet0 - Estudio: Mixed Precision - Batch Size 128 - Alpha Normalizado por Tau=0.7

============================================================
RENDIMIENTO GLOBAL
   - Accuracy Entrenamiento: 0.6677
   - Accuracy Validación:    0.6125
   - Accuracy Test:          0.6241
============================================================

## 📋 REPORTE DETALLADO POR CLASE (SET DE TEST):
                       precision    recall  f1-score   support

  Queratosis actínica       0.41      0.35      0.38        48
Carcinoma basocelular       0.59      0.62      0.61        66
   Queratosis benigna       0.51      0.60      0.55       172
       Dermatofibroma       0.07      0.30      0.11        10
   Nevus melanocítico       0.98      0.61      0.75      1016
             Melanoma       0.30      0.82      0.44       186
      Lesión vascular       0.73      0.76      0.75        29

             accuracy                           0.62      1527
            macro avg       0.51      0.58      0.51      1527
         weighted avg       0.80      0.62      0.67      1527


## 📋 REPORTE DETALLADO POR CLASE (SET DE VALIDACIÓN):
                       precision    recall  f1-score   support

  Queratosis actínica       0.49      0.56      0.52        57
Carcinoma basocelular       0.79      0.62      0.69        99
   Queratosis benigna       0.47      0.57      0.52       157
       Dermatofibroma       0.11      0.46      0.18        13
   Nevus melanocítico       0.96      0.59      0.74      1024
             Melanoma       0.25      0.78      0.38       156
      Lesión vascular       0.58      0.74      0.65        19

             accuracy                           0.61      1525
            macro avg       0.52      0.62      0.53      1525
         weighted avg       0.80      0.61      0.66      1525


## 📋 REPORTE DETALLADO POR CLASE (SET DE ENTRENAMIENTO):
                       precision    recall  f1-score   support

  Queratosis actínica       0.62      0.56      0.59       222
Carcinoma basocelular       0.73      0.72      0.73       349
   Queratosis benigna       0.54      0.61      0.57       770
       Dermatofibroma       0.26      0.78      0.39        92
   Nevus melanocítico       0.98      0.64      0.78      4665
             Melanoma       0.31      0.83      0.45       771
      Lesión vascular       0.72      0.93      0.81        94

             accuracy                           0.67      6963
            macro avg       0.59      0.72      0.62      6963
         weighted avg       0.82      0.67      0.70      6963

