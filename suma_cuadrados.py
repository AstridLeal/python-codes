'''
Desafio Semanal 3 - Problema 2
La suma de los cuadrados de los primeros diez números naturales es:
1^2 + 2^2 + ... + 10^2 = 385
El cuadrado de la suma de los primeros diez números naturales es:
(1 + 2 + ... + 10)^2 = 55^2 = 3025.
Por lo tanto, la diferencia entre la suma de los cuadrados de los primeros diez números naturales y el cuadrado de la suma es
3025 - 385 = 2640.
Encuentra la diferencia entre la suma de los cuadrados de los primeros cien números naturales y el cuadrado de la suma.
'''

# suma de los cuadrados de los primeros cien números naturales
def suma_de_los_cuadrados(n):
    suma_cuadrados = 0
    for i in range(1, n + 1):
        suma_cuadrados += i ** 2
    return suma_cuadrados

# cuadrado de la suma de los primeros cien números naturales
def cuadrado_de_la_suma(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma ** 2

# prueba con los datos del problema
suma_prueba = suma_de_los_cuadrados(10)
cuadrado_prueba = cuadrado_de_la_suma(10)
diferencia_prueba = cuadrado_prueba - suma_prueba
print("La suma de los cuadrados de los primeros diez números naturales es: ", suma_prueba)
print("El cuadrado de la suma de los primeros diez números naturales es: ", cuadrado_prueba)
print("La diferencia entre la suma de los cuadrados de los primeros diez números naturales y el cuadrado de la suma es: ", diferencia_prueba)

# suma de los cuadrados y el cuadrado de la suma
n = 100
suma_cuadrados = suma_de_los_cuadrados(n)
cuadrado_suma = cuadrado_de_la_suma(n)

diferencia = cuadrado_suma - suma_cuadrados

print("La diferencia entre la suma de los cuadrados y el cuadrado de la suma de los primeros", n, "números naturales es:", diferencia)