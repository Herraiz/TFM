

# Modelo Mobilenet - Estudio: Mobilenet - Mixed Precision - Batch Size 128

============================================================
RENDIMIENTO GLOBAL
   - Accuracy Entrenamiento: 0.7834
   - Accuracy Validación:    0.6839
   - Accuracy Test:          0.6902
============================================================

## 📋 REPORTE DETALLADO POR CLASE (SET DE TEST):
                       precision    recall  f1-score   support

  Queratosis actínica       0.48      0.50      0.49        48
Carcinoma basocelular       0.61      0.73      0.66        66
   Queratosis benigna       0.50      0.69      0.58       172
       Dermatofibroma       0.11      0.30      0.16        10
   Nevus melanocítico       0.95      0.70      0.81      1016
             Melanoma       0.39      0.64      0.49       186
      Lesión vascular       0.33      0.93      0.48        29

             accuracy                           0.69      1527
            macro avg       0.48      0.64      0.52      1527
         weighted avg       0.79      0.69      0.72      1527


## 📋 REPORTE DETALLADO POR CLASE (SET DE VALIDACIÓN):
                       precision    recall  f1-score   support

  Queratosis actínica       0.52      0.63      0.57        57
Carcinoma basocelular       0.78      0.57      0.65        99
   Queratosis benigna       0.40      0.68      0.50       157
       Dermatofibroma       0.25      0.54      0.34        13
   Nevus melanocítico       0.96      0.70      0.81      1024
             Melanoma       0.36      0.63      0.46       156
      Lesión vascular       0.27      0.95      0.42        19

             accuracy                           0.68      1525
            macro avg       0.51      0.67      0.54      1525
         weighted avg       0.80      0.68      0.72      1525


## 📋 REPORTE DETALLADO POR CLASE (SET DE ENTRENAMIENTO):
                       precision    recall  f1-score   support

  Queratosis actínica       0.84      0.87      0.86       222
Carcinoma basocelular       0.85      0.91      0.88       349
   Queratosis benigna       0.60      0.86      0.71       770
       Dermatofibroma       0.63      0.97      0.76        92
   Nevus melanocítico       0.99      0.75      0.85      4665
             Melanoma       0.51      0.80      0.63       771
      Lesión vascular       0.25      1.00      0.40        94

             accuracy                           0.78      6963
            macro avg       0.67      0.88      0.73      6963
         weighted avg       0.86      0.78      0.80      6963

