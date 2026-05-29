

# Modelo CoAtNet0 - Estudio: Mixed Precision - Batch Size 64 - Alpha Normalizado por Tau=0.7

============================================================
RENDIMIENTO GLOBAL
   - Accuracy Entrenamiento: 0.7840
   - Accuracy Validación:    0.7154
   - Accuracy Test:          0.7256
============================================================

## 📋 REPORTE DETALLADO POR CLASE (SET DE TEST):
                       precision    recall  f1-score   support

  Queratosis actínica       0.45      0.50      0.48        48
Carcinoma basocelular       0.77      0.52      0.62        66
   Queratosis benigna       0.59      0.66      0.62       172
       Dermatofibroma       0.12      0.10      0.11        10
   Nevus melanocítico       0.97      0.75      0.84      1016
             Melanoma       0.38      0.85      0.52       186
      Lesión vascular       0.77      0.69      0.73        29

             accuracy                           0.73      1527
            macro avg       0.58      0.58      0.56      1527
         weighted avg       0.82      0.73      0.75      1527


## 📋 REPORTE DETALLADO POR CLASE (SET DE VALIDACIÓN):
                       precision    recall  f1-score   support

  Queratosis actínica       0.47      0.65      0.54        57
Carcinoma basocelular       0.92      0.48      0.64        99
   Queratosis benigna       0.54      0.63      0.58       157
       Dermatofibroma       0.50      0.31      0.38        13
   Nevus melanocítico       0.95      0.76      0.84      1024
             Melanoma       0.30      0.72      0.43       156
      Lesión vascular       1.00      0.68      0.81        19

             accuracy                           0.72      1525
            macro avg       0.67      0.60      0.60      1525
         weighted avg       0.82      0.72      0.75      1525


## 📋 REPORTE DETALLADO POR CLASE (SET DE ENTRENAMIENTO):
                       precision    recall  f1-score   support

  Queratosis actínica       0.64      0.75      0.69       222
Carcinoma basocelular       0.90      0.69      0.78       349
   Queratosis benigna       0.68      0.72      0.70       770
       Dermatofibroma       0.67      0.71      0.69        92
   Nevus melanocítico       0.98      0.79      0.87      4665
             Melanoma       0.40      0.86      0.54       771
      Lesión vascular       0.95      0.97      0.96        94

             accuracy                           0.78      6963
            macro avg       0.75      0.78      0.75      6963
         weighted avg       0.86      0.78      0.81      6963

