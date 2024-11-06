'''
Desafio Semanal 3 - Problema 1
Cada nuevo término en la secuencia de Fibonacci se genera sumando los dos términos anteriores. Comenzando con 1 y 2, los primeros 10 términos serán:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
Considerando los términos de la secuencia de Fibonacci cuyos valores no exceden los cuatro millones, encuentra la suma de los términos pares.
'''

def suma(limite):
    a, b = 1, 2  # los dos primeros términos de la secuencia de Fibonacci
    suma_pares = 0  # suma de los términos pares

    # iteramos mientras el término actual no exceda el límite
    while a <= limite:
        # si el término actual es par, lo añadimos a la suma
        if a % 2 == 0:
            suma_pares += a
        # actualizamos los términos de la secuencia de Fibonacci
        a, b = b, a + b # el nuevo "a" se convierte en el valor actual de "b", y el nuevo "b" se convierte en la suma de los valores actuales de "a" y "b"

    return suma_pares

limite = 4000000 # de acuerdo al problema
resultado = suma(limite)
print("La suma de los términos pares de la secuencia de Fibonacci que no exceden los cuatro millones es:", resultado)
