

# Modelo CoAtNet0 - Estudio: Descongelamos parcialmente el modelo base - Batch Size 64

============================================================
RENDIMIENTO GLOBAL
   - Accuracy Entrenamiento: 0.6898
   - Accuracy Validación:    0.6387
   - Accuracy Test:          0.6444
============================================================

## 📋 REPORTE DETALLADO POR CLASE (SET DE TEST):
                       precision    recall  f1-score   support

  Queratosis actínica       0.35      0.40      0.37        48
Carcinoma basocelular       0.53      0.44      0.48        66
   Queratosis benigna       0.58      0.34      0.43       172
       Dermatofibroma       0.25      0.10      0.14        10
   Nevus melanocítico       0.97      0.68      0.80      1016
             Melanoma       0.29      0.88      0.43       186
      Lesión vascular       0.88      0.72      0.79        29

             accuracy                           0.64      1527
            macro avg       0.55      0.51      0.49      1527
         weighted avg       0.80      0.64      0.68      1527


## 📋 REPORTE DETALLADO POR CLASE (SET DE VALIDACIÓN):
                       precision    recall  f1-score   support

  Queratosis actínica       0.40      0.58      0.47        57
Carcinoma basocelular       0.79      0.49      0.61        99
   Queratosis benigna       0.56      0.29      0.38       157
       Dermatofibroma       0.50      0.23      0.32        13
   Nevus melanocítico       0.97      0.68      0.80      1024
             Melanoma       0.24      0.84      0.37       156
      Lesión vascular       0.80      0.63      0.71        19

             accuracy                           0.64      1525
            macro avg       0.61      0.54      0.52      1525
         weighted avg       0.81      0.64      0.68      1525


## 📋 REPORTE DETALLADO POR CLASE (SET DE ENTRENAMIENTO):
                       precision    recall  f1-score   support

  Queratosis actínica       0.48      0.50      0.49       222
Carcinoma basocelular       0.78      0.72      0.75       349
   Queratosis benigna       0.62      0.39      0.48       770
       Dermatofibroma       0.62      0.39      0.48        92
   Nevus melanocítico       0.97      0.72      0.83      4665
             Melanoma       0.29      0.86      0.43       771
      Lesión vascular       0.97      0.96      0.96        94

             accuracy                           0.69      6963
            macro avg       0.68      0.65      0.63      6963
         weighted avg       0.83      0.69      0.73      6963

