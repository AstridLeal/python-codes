#diccionario vacio
biblioteca = {}

#función que solicita al usuario información sobre el libro y la agrega al diccionario
def agregar_libro():
    titulo = input("Introduce el título del libro: ")
    autor = input("Introduce el autor del libro: ")
    año = int(input("Introduce el año de publicación del libro: "))
    genero = input("Introduce el género del libro: ")

#agrega la información dada al diciconario
    biblioteca[titulo] = {
        "autor": autor,
        "año": año,
        "genero": genero
    }

#función que muestra la información de todos los libros en el diccionario
def mostrar_biblioteca():
    for titulo, libro in biblioteca.items():
        print(f"Título: {titulo}")
        print(f"Autor: {libro['autor']}")
        print(f"Año: {libro['año']}")
        print(f"Género: {libro['genero']}")
        print()

#función que permite al usuario actualizar un campo específico de un libro en el diccionario
def actualizar_libro():
    titulo = input("Introduce el título del libro a actualizar: ")
    if titulo not in biblioteca:
        print("El libro no existe en la biblioteca.")
        return

    campo = input("Introduce el campo a actualizar (autor, año, genero): ")
    if campo not in biblioteca[titulo]:
        print("El campo no existe para el libro.")
        return

#actualiza la información del libro
    nuevo_valor = input("Introduce el nuevo valor para el campo: ")
    biblioteca[titulo][campo] = nuevo_valor

#función que permite al usuario eliminar un libro del diccionario
def eliminar_libro():
    titulo = input("Introduce el título del libro a eliminar: ")
    if titulo not in biblioteca:
        print("El libro no existe en la biblioteca.")
        return
    
#elimina el libro
    del biblioteca[titulo]

#menú de opciones
while True:
    opcion = input("""
    1. Agregar libro
    2. Mostrar biblioteca
    3. Actualizar libro
    4. Eliminar libro
    5. Salir

    Introduce una opción: """)

    if opcion == "1":
        agregar_libro()
    elif opcion == "2":
        mostrar_biblioteca()
    elif opcion == "3":
        actualizar_libro()
    elif opcion == "4":
        eliminar_libro()
    elif opcion == "5":
        break
    else:
        print("Opción no válida.")