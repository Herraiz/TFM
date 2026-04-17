import tensorflow as tf
import time

# 1. Comprobar versión
print(f"Versión de TensorFlow: {tf.__version__}")

# 2. Listar GPUs detectadas
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    print(f"✅ ¡GPU Detectada!: {gpus[0]}")
    # Esto ayuda a evitar errores de memoria al principio
    tf.config.experimental.set_memory_growth(gpus[0], True)
else:
    print("❌ No se detectó ninguna GPU. Revisa los drivers.")
    exit()

# 3. El "Hello World" matemático (Multiplicación de matrices)
print("\nIniciando prueba de fuego en la 3080 Ti...")

# Creamos dos matrices aleatorias gigantes directamente en la GPU
with tf.device('/GPU:0'):
    a = tf.random.normal([10000, 10000])
    b = tf.random.normal([10000, 10000])
    
    start_time = time.time()
    # Multiplicamos las matrices (operación pesada)
    c = tf.matmul(a, b)
    end_time = time.time()

print(f"⚡ Operación completada en: {end_time - start_time:.4f} segundos")
print("🚀 Tu entorno está listo para la CoAtNet.")