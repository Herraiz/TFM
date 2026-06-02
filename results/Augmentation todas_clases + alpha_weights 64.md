

# Modelo CoAtNet0 - Estudio: Augmentation todas_clases + alpha_weights 64

============================================================
RENDIMIENTO GLOBAL
   - Accuracy Entrenamiento: 0.8715
   - Accuracy Validación:    0.7797
   - Accuracy Test:          0.7865
============================================================

## 📋 REPORTE DETALLADO POR CLASE (SET DE TEST):
                       precision    recall  f1-score   support

  Queratosis actínica       0.51      0.40      0.45        48
Carcinoma basocelular       0.68      0.68      0.68        66
   Queratosis benigna       0.56      0.83      0.67       172
       Dermatofibroma       0.33      0.10      0.15        10
   Nevus melanocítico       0.95      0.83      0.89      1016
             Melanoma       0.51      0.68      0.58       186
      Lesión vascular       0.79      0.79      0.79        29

             accuracy                           0.79      1527
            macro avg       0.62      0.62      0.60      1527
         weighted avg       0.82      0.79      0.80      1527


## 📋 REPORTE DETALLADO POR CLASE (SET DE VALIDACIÓN):
                       precision    recall  f1-score   support

  Queratosis actínica       0.61      0.68      0.64        57
Carcinoma basocelular       0.84      0.68      0.75        99
   Queratosis benigna       0.49      0.77      0.60       157
       Dermatofibroma       0.62      0.38      0.48        13
   Nevus melanocítico       0.94      0.84      0.89      1024
             Melanoma       0.42      0.54      0.48       156
      Lesión vascular       0.87      0.68      0.76        19

             accuracy                           0.78      1525
            macro avg       0.68      0.65      0.66      1525
         weighted avg       0.82      0.78      0.79      1525


## 📋 REPORTE DETALLADO POR CLASE (SET DE ENTRENAMIENTO):
                       precision    recall  f1-score   support

  Queratosis actínica       0.81      0.76      0.78       222
Carcinoma basocelular       0.91      0.91      0.91       349
   Queratosis benigna       0.70      0.89      0.78       770
       Dermatofibroma       0.84      0.93      0.89        92
   Nevus melanocítico       0.97      0.89      0.93      4665
             Melanoma       0.60      0.76      0.67       771
      Lesión vascular       0.97      0.98      0.97        94

             accuracy                           0.87      6963
            macro avg       0.83      0.87      0.85      6963
         weighted avg       0.89      0.87      0.88      6963

