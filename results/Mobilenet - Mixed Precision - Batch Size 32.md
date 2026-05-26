

# Modelo Mobilenet - Estudio: Mobilenet - Mixed Precision - Batch Size 32

============================================================
RENDIMIENTO GLOBAL
   - Accuracy Entrenamiento: 0.6871
   - Accuracy Validación:    0.6216
   - Accuracy Test:          0.6372
============================================================

## 📋 REPORTE DETALLADO POR CLASE (SET DE TEST):
                       precision    recall  f1-score   support

  Queratosis actínica       0.53      0.40      0.45        48
Carcinoma basocelular       0.55      0.68      0.61        66
   Queratosis benigna       0.49      0.55      0.52       172
       Dermatofibroma       0.28      0.70      0.40        10
   Nevus melanocítico       0.96      0.64      0.77      1016
             Melanoma       0.32      0.74      0.45       186
      Lesión vascular       0.25      0.76      0.38        29

             accuracy                           0.64      1527
            macro avg       0.48      0.64      0.51      1527
         weighted avg       0.78      0.64      0.67      1527


## 📋 REPORTE DETALLADO POR CLASE (SET DE VALIDACIÓN):
                       precision    recall  f1-score   support

  Queratosis actínica       0.61      0.39      0.47        57
Carcinoma basocelular       0.65      0.65      0.65        99
   Queratosis benigna       0.41      0.53      0.46       157
       Dermatofibroma       0.28      0.62      0.38        13
   Nevus melanocítico       0.96      0.64      0.76      1024
             Melanoma       0.26      0.67      0.38       156
      Lesión vascular       0.19      0.84      0.31        19

             accuracy                           0.62      1525
            macro avg       0.48      0.62      0.49      1525
         weighted avg       0.78      0.62      0.67      1525


## 📋 REPORTE DETALLADO POR CLASE (SET DE ENTRENAMIENTO):
                       precision    recall  f1-score   support

  Queratosis actínica       0.79      0.47      0.59       222
Carcinoma basocelular       0.70      0.80      0.75       349
   Queratosis benigna       0.58      0.64      0.61       770
       Dermatofibroma       0.41      0.80      0.54        92
   Nevus melanocítico       0.98      0.67      0.79      4665
             Melanoma       0.35      0.83      0.50       771
      Lesión vascular       0.22      1.00      0.36        94

             accuracy                           0.69      6963
            macro avg       0.58      0.74      0.59      6963
         weighted avg       0.83      0.69      0.72      6963

