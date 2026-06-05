
# Modelo CoAtNet1 - Estudio: CoAtNet1 Augmentation + custom loss + optuna valors 64 (Sensibilidad Ajustada)

============================================================
CONFIGURACIÓN DE UMBRALES:
   - Melanoma: 0.28
   - Carcinoma Basocelular: Default
   - Queratosis Actínica: Default

RENDIMIENTO GLOBAL (Ajuste de Sensibilidad)
   - Accuracy Test:          0.62
============================================================

## 📋 REPORTE DETALLADO POR CLASE (SET DE TEST):
                       precision    recall  f1-score   support

  Queratosis actínica       0.24      0.31      0.27        48
Carcinoma basocelular       0.31      0.56      0.40        66
   Queratosis benigna       0.47      0.47      0.47       172
       Dermatofibroma       0.20      0.40      0.27        10
   Nevus melanocítico       0.94      0.66      0.78      1016
             Melanoma       0.30      0.62      0.40       186
      Lesión vascular       0.43      0.69      0.53        29

             accuracy                           0.62      1527
            macro avg       0.41      0.53      0.45      1527
         weighted avg       0.74      0.62      0.66      1527

