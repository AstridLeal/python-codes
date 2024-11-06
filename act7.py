#Crea un programa que pida al usuario que introduzca una cadena de texto. Si la cadena de texto contiene la palabra "fiesta", el programa debe imprimir un mensaje que diga "¡Fiesta, fiesta, fiesta!". Si no la contiene, el programa debe imprimir un mensaje que diga "No hay fiesta sin tí :(".

cadena = input("Introduce una cadena de texto: ")

if "fiesta" in cadena.lower(): #hacer minuculas las mayusculas
    print("¡Fiesta, fiesta, fiesta!")
else:
    print("No hay fiesta sin tí :(")