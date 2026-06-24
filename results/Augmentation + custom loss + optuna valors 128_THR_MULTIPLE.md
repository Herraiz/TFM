
# Modelo CoAtNet0 - Estudio: Augmentation + custom loss + optuna valors 128 (Sensibilidad Ajustada)

============================================================
CONFIGURACIÓN DE UMBRALES:
   - Melanoma: 0.1
   - Carcinoma Basocelular: Default
   - Queratosis Actínica: Default

RENDIMIENTO GLOBAL (Ajuste de Sensibilidad)
   - Accuracy Test:          0.66
============================================================

## 📋 REPORTE DETALLADO POR CLASE (SET DE TEST):
                       precision    recall  f1-score   support

  Queratosis actínica       0.71      0.25      0.37        48
Carcinoma basocelular       0.88      0.55      0.67        66
   Queratosis benigna       0.68      0.35      0.46       172
       Dermatofibroma       0.17      0.10      0.12        10
   Nevus melanocítico       0.97      0.69      0.81      1016
             Melanoma       0.29      0.97      0.44       186
      Lesión vascular       0.95      0.72      0.82        29

             accuracy                           0.66      1527
            macro avg       0.66      0.52      0.53      1527
         weighted avg       0.83      0.66      0.70      1527

