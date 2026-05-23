

# Modelo CoAtNet3 - Estudio: C3_Clean_No_XLA_Stateless_Augmentation

============================================================
RENDIMIENTO GLOBAL
   - Accuracy Entrenamiento: 0.0742
   - Accuracy Validación:    0.0879
   - Accuracy Test:          0.0766
============================================================

## 📋 REPORTE DETALLADO POR CLASE (SET DE TEST):
                       precision    recall  f1-score   support

  Queratosis actínica       0.00      0.00      0.00        48
Carcinoma basocelular       0.06      0.88      0.11        66
   Queratosis benigna       0.01      0.01      0.01       172
       Dermatofibroma       0.00      0.00      0.00        10
   Nevus melanocítico       0.86      0.03      0.06      1016
             Melanoma       0.09      0.14      0.11       186
      Lesión vascular       0.00      0.00      0.00        29

             accuracy                           0.08      1527
            macro avg       0.15      0.15      0.04      1527
         weighted avg       0.59      0.08      0.06      1527


## 📋 REPORTE DETALLADO POR CLASE (SET DE VALIDACIÓN):
                       precision    recall  f1-score   support

  Queratosis actínica       0.00      0.00      0.00        57
Carcinoma basocelular       0.08      0.88      0.15        99
   Queratosis benigna       0.00      0.00      0.00       157
       Dermatofibroma       0.00      0.00      0.00        13
   Nevus melanocítico       1.00      0.03      0.06      1024
             Melanoma       0.04      0.08      0.05       156
      Lesión vascular       0.08      0.11      0.09        19

             accuracy                           0.09      1525
            macro avg       0.17      0.16      0.05      1525
         weighted avg       0.68      0.09      0.06      1525


## 📋 REPORTE DETALLADO POR CLASE (SET DE ENTRENAMIENTO):
                       precision    recall  f1-score   support

  Queratosis actínica       0.00      0.00      0.00       222
Carcinoma basocelular       0.06      0.86      0.12       349
   Queratosis benigna       0.02      0.01      0.02       770
       Dermatofibroma       0.00      0.00      0.00        92
   Nevus melanocítico       0.88      0.03      0.05      4665
             Melanoma       0.06      0.10      0.07       771
      Lesión vascular       0.02      0.02      0.02        94

             accuracy                           0.07      6963
            macro avg       0.15      0.15      0.04      6963
         weighted avg       0.60      0.07      0.05      6963

