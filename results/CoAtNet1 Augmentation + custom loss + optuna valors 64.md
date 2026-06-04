

# Modelo CoAtNet1 - Estudio: CoAtNet1 Augmentation + custom loss + optuna valors 64

============================================================
RENDIMIENTO GLOBAL
   - Accuracy Entrenamiento: 0.7220
   - Accuracy Validación:    0.6879
   - Accuracy Test:          0.6785
============================================================

## 📋 REPORTE DETALLADO POR CLASE (SET DE TEST):
                       precision    recall  f1-score   support

  Queratosis actínica       0.24      0.31      0.27        48
Carcinoma basocelular       0.31      0.56      0.40        66
   Queratosis benigna       0.46      0.51      0.49       172
       Dermatofibroma       0.20      0.40      0.27        10
   Nevus melanocítico       0.88      0.80      0.84      1016
             Melanoma       0.34      0.32      0.33       186
      Lesión vascular       0.43      0.69      0.53        29

             accuracy                           0.68      1527
            macro avg       0.41      0.51      0.45      1527
         weighted avg       0.71      0.68      0.69      1527


## 📋 REPORTE DETALLADO POR CLASE (SET DE VALIDACIÓN):
                       precision    recall  f1-score   support

  Queratosis actínica       0.25      0.26      0.25        57
Carcinoma basocelular       0.38      0.57      0.45        99
   Queratosis benigna       0.40      0.49      0.44       157
       Dermatofibroma       0.16      0.38      0.23        13
   Nevus melanocítico       0.90      0.81      0.85      1024
             Melanoma       0.39      0.37      0.38       156
      Lesión vascular       0.50      0.63      0.56        19

             accuracy                           0.69      1525
            macro avg       0.42      0.50      0.45      1525
         weighted avg       0.73      0.69      0.70      1525


## 📋 REPORTE DETALLADO POR CLASE (SET DE ENTRENAMIENTO):
                       precision    recall  f1-score   support

  Queratosis actínica       0.25      0.32      0.28       222
Carcinoma basocelular       0.38      0.60      0.46       349
   Queratosis benigna       0.50      0.53      0.51       770
       Dermatofibroma       0.19      0.29      0.23        92
   Nevus melanocítico       0.90      0.84      0.87      4665
             Melanoma       0.47      0.39      0.43       771
      Lesión vascular       0.45      0.85      0.59        94

             accuracy                           0.72      6963
            macro avg       0.45      0.55      0.48      6963
         weighted avg       0.75      0.72      0.73      6963

