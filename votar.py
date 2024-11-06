
#Escribe un programa que le pida nombre y edad al usuario, y posteriormente imprima un mensaje personalizado indicando si puede votar o no.

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

if (edad >= 18):
    print(f"Buen día, {nombre}, tú sí puedes votar.")
else:
    print(f"Buen día, {nombre}, tú no puedes votar porque tienes menos de 18 años.")