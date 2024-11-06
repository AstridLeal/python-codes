#Crea un programa que pida al usuario que introduzca dos números enteros. El programa debe imprimir un mensaje que diga si el primer número es mayor, menor o igual al segundo número, pero en lugar de usar las palabras "mayor" o "menor", debes usar palabras divertidas como "tremendote" o "microscópico".

x = int(input("Introduce el primer número: "))
y = int(input("Introduce el segundo número: "))

if x > y:
    print(f"¡El primer número es {x}, un gigante comparado con el chiquitín {y}!")
elif x < y:
    print(f"¡El segundo número es {y}, un gigante comparado con el chiquitín {x}!")
else:
    print(f"¡Los dos números son iguales!")