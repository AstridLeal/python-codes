# Crear un diccionario con información de la película
pelicula = {"titulo": "Kill Your Darlings", "estreno": 2013, "director": "John Krokidas", "puntuacion": 6.4}

# Acceder a los valores para imprimir el mensaje
mensaje = f"Me encanta {pelicula['titulo']} ({pelicula['estreno']}) de {pelicula['director']} con una puntuación de {pelicula['puntuacion']} en IMDb."
print(mensaje)