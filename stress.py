import tensorflow as tf
import time

# Configuración: Matrices de 10k x 10k (ocupan mucha VRAM y núcleos)
SIZE = 10000 
ITERATIONS = 100 

print(f"🚀 Iniciando test de estrés en la RTX 3080 Ti...")
print(f"Operación: {ITERATIONS} multiplicaciones de matrices de {SIZE}x{SIZE}")

with tf.device('/GPU:0'):
    # Inicializamos las matrices en la GPU
    matrix1 = tf.random.normal([SIZE, SIZE])
    matrix2 = tf.random.normal([SIZE, SIZE])

    start_time = time.time()
    
    for i in range(ITERATIONS):
        # El comando 'matmul' es el que realmente pone a trabajar los núcleos CUDA
        result = tf.matmul(matrix1, matrix2)
        
        # Cada 10 iteraciones imprimimos progreso
        if (i + 1) % 10 == 0:
            elapsed = time.time() - start_time
            print(f"🔹 Iteración {i+1}/{ITERATIONS} - Tiempo acumulado: {elapsed:.2f}s")

    end_time = time.time()

print("\n✅ ¡Test completado!")
print(f"⏱️ Tiempo total: {end_time - start_time:.2f} segundos.")