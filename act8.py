#Crea un programa que pida al usuario que introduzca dos números enteros. Si el primer número es mayor que el segundo número, el programa debe imprimir un mensaje que diga "¡Vas por el camino correcto!". Si el segundo número es mayor que el primer número, el programa debe imprimir un mensaje que diga "¡Cuidado! Estás en un camino peligroso". Si los dos números son iguales, el programa debe imprimir un mensaje que diga "Estás en un camino muy equilibrado".

x = int(input("Introduce el primer número: "))
y = int(input("Introduce el segundo número: "))

if x > y:
    print("¡Vas por el camino correcto!")
elif y > x:
    print("¡Cuidado! Estás en un camino peligroso")
else:
    print("Estás en un camino muy equilibrado")