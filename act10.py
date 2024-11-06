#Crea un programa que pida al usuario que introduzca un número entero. Si el número es divisible por 3, el programa debe imprimir un mensaje que diga "¡DJ, pon la música de los 80s!". Si el número es divisible por 5, el programa debe imprimir un mensaje que diga "¡DJ, pon la música electrónica!". Si el número es divisible por 3 y por 5, el programa debe imprimir un mensaje que diga "¡DJ, pon la música de los 90s!". Si el número no es divisible por 3 ni por 5, el programa debe imprimir un mensaje que diga "¡DJ, pon la música de moda!".

x = int(input("Introduce un número entero: "))
    
if x % 3 == 0 and x % 5 == 0:
    print("¡DJ, pon la música de los 90s!")
elif x % 3 == 0:
    print("¡DJ, pon la música de los 80s!")
elif x % 5 == 0:
    print("¡DJ, pon la música electrónica!")
else:
    print("¡DJ, pon la música de moda!")
    
    
    