import random

tesoros = ["Brújula antigua", "Cadaver de ogro", "Moco de oro", "Mapa antiguo", "Gema preciosa", "Calzones de la suerte", "Daga ceremonial", "Cetro de poder", "Espejo mágico de la bestia"]

print("Lista de tesoros disponibles:")
for tesoro in tesoros:
    print("-", tesoro)
    
num_objetos = int(input("\n¿Cuántos objetos deseas seleccionar en tu búsqueda?: "))

objetos_seleccionados = []
for _ in range(num_objetos):
    tesoro_seleccionado = random.choice(tesoros)
    objetos_seleccionados.append(tesoro_seleccionado)

print("\nTus objetos seleccionados en la aventura son:")
for objeto in objetos_seleccionados:
    print("-", objeto)