# Programa que toma dos numeros enteros como entrada y que saca el rango de numeros entre las dos entradas como una lista.
# La secuencia de salida debe comenzar con el primer numero de entrada y terminar con el segundo numero de entrada, sin incluirlo.

a = int(input())
b = int(input())

num = list(range(a,b))
print(num)