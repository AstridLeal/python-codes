import math

def mcd(a, b): # Función para calcular el MCD de dos números
    # Implementación del algoritmo de Euclides
    while b != 0: 
        a, b = b, a % b # Intercambiamos los valores de a y b, y calculamos el módulo
    return a

def mcd_multiple(*numeros): # Función para calcular el MCD de varios números
    # Inicializamos el MCD con el primer número
    resultado = numeros[0] 
    
    # Iteramos por los siguientes números y aplicamos el MCD con el resultado acumulado
    for num in numeros[1:]:
        resultado = mcd(resultado, num) # Calculamos el MCD entre el resultado acumulado y el número actual
    
    return resultado

numeros = list(map(int, input("Introduce los números separados por espacio: ").split())) # Pedimos los números al usuario
resultado = mcd_multiple(*numeros) # Calculamos el MCD de los números introducidos
print(f"El MCD de los números {numeros} es: {resultado}") # Mostramos el resultado
