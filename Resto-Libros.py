# Tenemos que distribuir los libros de texto a los alumnos. Hay 37 alumnos en la clase y cada uno debe recibir 2 libros de texto.
# El número total de libros disponibles para la distribución es de 76.
# Tarea: Escribe un programa que calcule y genere cuántos libros quedarán después de la distribución.

# EL OPERADO MÓDULO % SE USA PARA OBTENER EL RESTO
librosPorAlumno=2
alumnos=37
librosDisponibles=76
librosNecesarios=alumnos*librosPorAlumno

print(librosDisponibles%librosNecesarios)