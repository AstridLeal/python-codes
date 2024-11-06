#Crea un programa que pida al usuario que introduzca el nombre de su lenguaje de programación favorito. Si la cadena de texto es igual a "Python", el programa debe imprimir un mensaje que diga "¡Muy buena elección!". Si la cadena de texto es igual a "Java" o "C++", el programa debe imprimir un mensaje que diga "Buenas opciones también". Si la cadena de texto es igual a cualquier otra cosa, el programa debe imprimir un mensaje que diga "Esa opción es un poco rara, pero respetable".

x = input("Introduce el nombre de tu lenguaje de programación favorito: ")

if x.lower() == "python":
    print("¡Muy buena elección!")
elif x.lower() == "java" or x.lower() == "c++":
    print("Buenas opciones también")
else:
    print("Esa opción es un poco rara, pero respetable")