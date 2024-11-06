# Programa que suma dos números sin usar el operador + ni sum(), ni __add__()

def suma_sin_operador(a, b):
    # Usamos operaciones bit a bit para lograr la suma
    while b != 0: # Mientras haya algo que sumar
        # El "carry" contiene los bits que se llevarían a la siguiente posición
        carry = a & b # AND para obtener los bits que se llevarán
        # Sumamos a y b sin tener en cuenta el carry
        a = a ^ b # XOR para sumar sin llevar
        # Ahora el carry lo desplazamos una posición a la izquierda para sumarlo en la siguiente iteración
        b = carry << 1 
    return a # Retornamos el resultado

# Pedimos los números al usuario
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))

# Calculamos la suma
resultado = suma_sin_operador(numero1, numero2)

# Mostramos el resultado
print("La suma es:", resultado)
