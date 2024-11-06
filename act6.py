#Crea un programa que pida al usuario que introduzca un número entero. Si el número es par, el programa debe imprimir un mensaje que diga "¡Qué par tan elegante!". Si el número es impar, el programa debe imprimir un mensaje que diga "¡Impar-able!".

x = int(input("Introduce un número entero: "))

if x % 2 == 0: #para obtener el resto de la división, si es 0 es par y sino es impar
    print(f"¡Qué par tan elegante!")
else:
    print(f"¡Impar-able!")