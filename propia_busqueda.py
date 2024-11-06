# Programa que adivina un número utilizando búsqueda binaria sin más de una función

def adivinar_numero():
    # Pedimos al usuario dos números distintos
    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))

    # Asegurarnos de que num1 sea menor que num2
    if num1 > num2:
        num1, num2 = num2, num1

    print(f"Piensa en un número entre {num1} y {num2} (sin incluirlos).")

    # Algoritmo de búsqueda binaria para adivinar el número
    while num1 + 1 < num2: # Mientras haya al menos un número entre num1 y num2
        guess = (num1 + num2) // 2 # Adivinar el número del medio
        print(f"¿El número que piensas es {guess}?") # Preguntar al usuario
        respuesta = input("Responde con 'mayor', 'menor' o 'igual': ").lower() # Leer la respuesta

        if respuesta == 'igual':
            print(f"¡Adiviné! El número es {guess}.") 
            break
        elif respuesta == 'mayor':
            num1 = guess
        elif respuesta == 'menor':
            num2 = guess
        else:
            print("Respuesta no válida. Por favor, responde con 'mayor', 'menor' o 'igual'.")

# Ejecutar el programa
adivinar_numero()
