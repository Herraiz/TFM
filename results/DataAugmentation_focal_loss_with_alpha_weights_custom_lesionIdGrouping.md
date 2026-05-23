

# Modelo CoAtNet0 - Estudio: DataAugmentation_focal_loss_with_alpha_weights_custom_lesionIdGrouping

============================================================
📈 RENDIMIENTO GLOBAL
   - Accuracy Entrenamiento: 0.7233
   - Accuracy Validación:    0.6610
   - Accuracy Test:          0.6706
============================================================

## 📋 REPORTE DETALLADO POR CLASE (SET DE TEST):
```text
                       precision    recall  f1-score   support

  Queratosis actínica       0.47      0.52      0.50        48
Carcinoma basocelular       0.69      0.52      0.59        66
   Queratosis benigna       0.52      0.70      0.59       172
       Dermatofibroma       0.11      0.70      0.19        10
   Nevus melanocítico       0.98      0.67      0.79      1016
             Melanoma       0.35      0.74      0.47       186
      Lesión vascular       0.66      0.86      0.75        29
             accuracy                           0.67      1527
            macro avg       0.54      0.67      0.55      1527
         weighted avg       0.81      0.67      0.71      1527

## 📋 REPORTE DETALLADO POR CLASE (SET DE VALIDACIÓN):
                       precision    recall  f1-score   support

  Queratosis actínica       0.61      0.65      0.63        57
Carcinoma basocelular       0.84      0.60      0.70        99
   Queratosis benigna       0.44      0.69      0.54       157
       Dermatofibroma       0.17      0.92      0.29        13
   Nevus melanocítico       0.97      0.65      0.78      1024
             Melanoma       0.29      0.67      0.40       156
      Lesión vascular       0.68      0.89      0.77        19
             accuracy                           0.66      1525
            macro avg       0.57      0.73      0.59      1525
         weighted avg       0.82      0.66      0.70      1525

## 📋 REPORTE DETALLADO POR CLASE (SET DE ENTRENAMIENTO):
                       precision    recall  f1-score   support

  Queratosis actínica       0.72      0.70      0.71       222
Carcinoma basocelular       0.84      0.74      0.79       349
   Queratosis benigna       0.56      0.77      0.65       770
       Dermatofibroma       0.29      1.00      0.44        92
   Nevus melanocítico       0.98      0.69      0.81      4665
             Melanoma       0.38      0.81      0.52       771
      Lesión vascular       0.69      0.99      0.82        94
             accuracy                           0.72      6963
            macro avg       0.64      0.82      0.68      6963
         weighted avg       0.84      0.72      0.75      6963

