import cv2
import numpy as np

# --- 1. Cargar imagen ---
ruta_imagen = 'ISIC_0029954.jpg' 
img = cv2.imread(ruta_imagen)

if img is None:
    print("¡Ups! Parece que no encuentro la imagen. Dale un vistazo a la ruta, por favor.")
else:
    # --- 2. Crear la máscara ---
    # Pasamos a blanco y negro porque las texturas se notan mejor
    gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Creamos molde para buscar formas finas y oscuras
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))
    
    # Aplicamos filtro blackhat
    blackhat = cv2.morphologyEx(gris, cv2.MORPH_BLACKHAT, kernel)
    
    # Separamos el pelo de lo que es fondo (negro)
    _, mascara = cv2.threshold(blackhat, 10, 255, cv2.THRESH_BINARY)

    # --- 3. Borramos el pelo ---
    # El 'inpaintRadius' es como el grosor del pincel difuminador. Un valor de 3 o 4 va bien.
    # INPAINT_TELEA es el algoritmo matemático que usamos.
    imagen_limpia = cv2.inpaint(img, mascara, inpaintRadius=3, flags=cv2.INPAINT_TELEA)

    # --- 4. Guardar resultado ---
    cv2.imwrite(ruta_imagen+'_sin_pelos.png', imagen_limpia)
    
    print(f"Pelos borrados: {ruta_imagen}_sin_pelos.png")