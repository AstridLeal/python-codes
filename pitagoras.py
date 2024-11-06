import pygame, random

# Inicialización de Pygame
pygame.init()

# Dimensiones de la pantalla
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Triángulos")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Función para dibujar un triángulo
def draw_triangle(x, y, hypotenuse, cathetus, color):
    # Calcular el otro cateto usando el teorema de Pitágoras
    other_cathetus = int((hypotenuse**2 - cathetus**2)**0.5)
    pygame.draw.polygon(screen, color, [(x, y), (x + cathetus, y), (x, y + other_cathetus)])

# Función para verificar si un triángulo colisiona con otros
def check_collision(new_triangle, triangles):
    new_rect = pygame.Rect(new_triangle[0], new_triangle[1], new_triangle[2], new_triangle[3])
    for triangle in triangles:
        triangle_rect = pygame.Rect(triangle[0], triangle[1], triangle[2], triangle[3])
        if new_rect.colliderect(triangle_rect):
            return True
    return False

# Lista para almacenar los triángulos dibujados
triangles = []

running = True
while running:
    for event in pygame.event.get(): # Obtener eventos
        if event.type == pygame.QUIT: # Si se presiona el botón de cerrar
            running = False # Salir del ciclo

    # Limpiar la pantalla
    screen.fill(WHITE)

    # Generar un nuevo triángulo
    hypotenuse = random.randint(50, 200)
    print(f"Hipotenusa: {hypotenuse}")
    cathetus_str = input("Ingrese la medida de un cateto: ")
    try:
        cathetus = int(cathetus_str)
    except ValueError:
        print("Ingrese un número válido.")
        continue

    # Buscar un lugar válido para dibujar el triángulo
    found_position = False
    for _ in range(100):  # Intentar encontrar un lugar hasta 100 veces
        # Generar coordenadas aleatorias y verificar colisiones
        x = random.randint(0, width - hypotenuse)
        y = random.randint(0, height - hypotenuse)
        # Crear un rectángulo que englobe al triángulo completo
        triangle_rect = pygame.Rect(x, y, hypotenuse, hypotenuse)
        # Verificar si el rectángulo intersecta con algún otro triángulo y si está dentro de la pantalla
        if not check_collision(triangle_rect, triangles) and 0 <= x <= width and 0 <= y <= height:
            found_position = True
        if found_position:
            break
    else:
        # Si no se encontró un lugar después de 100 intentos, el jugador pierde
        font = pygame.font.Font(None, 36)
        text = font.render("¡Has perdido!", True, BLACK)
        text_rect = text.get_rect(center=(width//2, height//2))
        screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False

    # Dibujar el triángulo
    draw_triangle(x, y, hypotenuse, cathetus, RED)
    triangles.append((x, y, hypotenuse, cathetus))

    # Dibujar todos los triángulos almacenados
    for triangle in triangles:
        x, y, hypotenuse, cathetus = triangle
        draw_triangle(x, y, hypotenuse, cathetus, RED)

    pygame.display.flip()

pygame.quit()