from PIL import Image # Importar la clase Image del módulo PIL, que permite trabajar con imágenes

def aplicar_filtro_calido(imagen):
    # Abrir imagen
    img = Image.open(imagen)
    img = img.convert("RGB")  # Asegurarse de que está en modo RGB
    
    # Crear nueva imagen para almacenar el resultado
    img_filtrada = Image.new("RGB", img.size)
    pixels_orig = img.load()
    pixels_filtrados = img_filtrada.load()
    
    # Ajustes de tinte
    a = 1.0  # Factor de brillo
    b, c, d = 50, 30, -20  # Ajuste de colores para un tinte cálido
    
    # Aplicar la transformación a cada píxel
    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels_orig[i, j]
            r = min(255, max(0, int(r * a + b)))
            g = min(255, max(0, int(g * a + c)))
            b = min(255, max(0, int(b * a + d)))
            pixels_filtrados[i, j] = (r, g, b)
    
    return img_filtrada

# Cargar la imagen y aplicar el filtro
imagen_filtrada = aplicar_filtro_calido("E:/Code/simpsons.jpg")

# Mostrar y guardar la imagen filtrada
imagen_filtrada.show()
imagen_filtrada.save("E:/Code/simpsons_filtro.jpg")