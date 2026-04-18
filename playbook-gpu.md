# Playbook: Configuración de Entorno Deep Learning (WSL2 + RTX 3080 Ti)

Este manual contiene la secuencia exacta de comandos para replicar el entorno de desarrollo en Ubuntu (WSL2) con soporte completo para GPU.

## Paso 1: Instalación de Miniconda (Linux Nativo)
# Ejecutar en la terminal de Ubuntu
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b -p $HOME/miniconda3
source ~/.bashrc
~/miniconda3/bin/conda init zsh  # O 'bash' si no usas zsh

## Paso 2: Creación del Entorno Virtual
conda create -n tfm_linux python=3.10 -y
conda activate tfm_linux

## Paso 3: Instalación de TensorFlow y Dependencias CUDA
pip install --upgrade pip
pip install "tensorflow[and-cuda]"

## Paso 4: Automatización de Librerías Dinámicas (Persistencia)
# Este comando vincula las librerías de NVIDIA instaladas por pip al path de Linux
# solo cuando el entorno está activo.
conda env config vars set LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib/wsl/lib:$CONDA_PREFIX/lib/python3.10/site-packages/nvidia/cuda_runtime/lib:$CONDA_PREFIX/lib/python3.10/site-packages/nvidia/cublas/lib:$CONDA_PREFIX/lib/python3.10/site-packages/nvidia/cudnn/lib:$CONDA_PREFIX/lib/python3.10/site-packages/nvidia/cusolver/lib:$CONDA_PREFIX/lib/python3.10/site-packages/nvidia/cusparse/lib:$CONDA_PREFIX/lib/python3.10/site-packages/nvidia/curand/lib:$CONDA_PREFIX/lib/python3.10/site-packages/nvidia/cufft/lib:$CONDA_PREFIX/lib/python3.10/site-packages/nvidia/nvjitlink/lib

# Reactivar para aplicar cambios
conda deactivate
conda activate tfm_linux

## Paso 5: Creación del Script de Estrés (stress_v2.py)
# Copia el siguiente contenido en un archivo llamado stress_v2.py
cat <<EOF > stress_v2.py
import tensorflow as tf
import time

# Configuración de memoria dinámica (evita bloqueos en WSL)
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    try:
        tf.config.experimental.set_memory_growth(gpus[0], True)
    except RuntimeError as e:
        print(e)

SIZE = 10000 
ITERATIONS = 100 

print(f"\n🚀 Iniciando Test de Estrés Real en la RTX 3080 Ti...")
print(f"Matrices: {SIZE}x{SIZE} | Iteraciones: {ITERATIONS}")

with tf.device('/GPU:0'):
    a = tf.random.normal([SIZE, SIZE])
    b = tf.random.normal([SIZE, SIZE])

    start_time = time.time()
    
    for i in range(ITERATIONS):
        # Operación de multiplicación de matrices (GEMM)
        res = tf.matmul(a, b)
        
        # Sincronización cada 10 iteraciones para medir carga real
        if i % 10 == 0:
            _ = res.numpy() 
            print(f"🔹 Ejecutando bloque {i}/{ITERATIONS}...")
        
        # Mutación de datos para evitar optimización por caché
        a = a + 0.01 

    # Sincronización final antes de cerrar el cronómetro
    _ = res.numpy()
    end_time = time.time()

print(f"\n✅ Test completado con éxito.")
print(f"⏱️ Tiempo total de cómputo real: {end_time - start_time:.2f} segundos.")
EOF

## Paso 6: Ejecución y Validación
python stress_v2.py