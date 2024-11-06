import random

# Códigos ANSI para colorear texto en rojo
RED = "\033[91m"
RESET = "\033[0m"

nombres = ["Galileo", "Lavender", "Heisenberg", "Burton", "Gus", "Goober", "Scooter", "Banana", "Bubbles", "Buddy"]
apellidos = ["Humpkins", "Gooms", "Marvin", "Barnes", "Thunderbottom", "McSnuggles", "Fluffernutter", "Jellybean", "Buttercup", "Picklepants"]

print("Bienvenido a 'Silly Name Generator'")

while True:
    nombre_elegido = random.choice(nombres)
    apellido_elegido = random.choice(apellidos)
    
    nombre_completo = f"{nombre_elegido} {apellido_elegido}"
    nombre_color = f"{RED}{nombre_completo}{RESET}"
    print(nombre_color)
    
    opcion = input("¿Generar otro? (s/n): ")
    if opcion.lower() != 's':
        break

