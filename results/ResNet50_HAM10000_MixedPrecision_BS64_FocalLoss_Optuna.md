

# Modelo ResNet50 - Estudio: ResNet50_HAM10000_MixedPrecision_BS64_FocalLoss_Optuna

============================================================
RENDIMIENTO GLOBAL
   - Accuracy Entrenamiento: 0.7541
   - Accuracy Validación:    0.6682
   - Accuracy Test:          0.5789
============================================================

## 📋 REPORTE DETALLADO POR CLASE (SET DE TEST):
                       precision    recall  f1-score   support

  Queratosis actínica       0.00      0.00      0.00        48
Carcinoma basocelular       0.16      0.08      0.10        66
   Queratosis benigna       0.33      0.33      0.33       172
       Dermatofibroma       0.02      0.50      0.04        10
   Nevus melanocítico       0.74      0.81      0.77      1016
             Melanoma       0.00      0.00      0.00       186
      Lesión vascular       0.00      0.00      0.00        29

             accuracy                           0.58      1527
            macro avg       0.18      0.24      0.18      1527
         weighted avg       0.54      0.58      0.55      1527


## 📋 REPORTE DETALLADO POR CLASE (SET DE VALIDACIÓN):
                       precision    recall  f1-score   support

  Queratosis actínica       0.64      0.53      0.58        57
Carcinoma basocelular       0.71      0.64      0.67        99
   Queratosis benigna       0.41      0.58      0.48       157
       Dermatofibroma       0.33      0.54      0.41        13
   Nevus melanocítico       0.97      0.67      0.80      1024
             Melanoma       0.30      0.78      0.43       156
      Lesión vascular       0.60      0.79      0.68        19

             accuracy                           0.67      1525
            macro avg       0.57      0.65      0.58      1525
         weighted avg       0.81      0.67      0.71      1525


## 📋 REPORTE DETALLADO POR CLASE (SET DE ENTRENAMIENTO):
                       precision    recall  f1-score   support

  Queratosis actínica       0.82      0.73      0.77       222
Carcinoma basocelular       0.76      0.90      0.82       349
   Queratosis benigna       0.66      0.72      0.69       770
       Dermatofibroma       0.53      0.88      0.66        92
   Nevus melanocítico       0.98      0.72      0.83      4665
             Melanoma       0.38      0.87      0.53       771
      Lesión vascular       0.59      1.00      0.74        94

             accuracy                           0.75      6963
            macro avg       0.67      0.83      0.72      6963
         weighted avg       0.85      0.75      0.78      6963

