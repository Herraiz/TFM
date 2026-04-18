import tensorflow as tf
import time

SIZE = 10000 
ITERATIONS = 100 

print(f"🚀 Test de Estrés Real en la RTX 3080 Ti...")

with tf.device('/GPU:0'):
    # Matrices iniciales
    a = tf.random.normal([SIZE, SIZE])
    b = tf.random.normal([SIZE, SIZE])

    start_time = time.time()
    
    for i in range(ITERATIONS):
        # Multiplicamos
        res = tf.matmul(a, b)
        
        #  Modificamos 'a' ligeramente para que la siguiente iteración sea distinta
        #  .numpy() obliga a la GPU a terminar y enviar el dato a la CPU (sincronización)
        if i % 10 == 0:
            _ = res.numpy() 
            print(f"🔹 Iteración {i}/{ITERATIONS}")
        
        # Cambiamos un poco la matriz para la siguiente vuelta
        a = a + 0.01 

    # Sincronización final
    _ = res.numpy()
    end_time = time.time()

print(f"\n✅ Test completado en: {end_time - start_time:.2f} segundos.")