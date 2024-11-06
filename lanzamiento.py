import time

#función de cuenta regresiva
def cuenta_regresiva(inicio):
    print("¡Preparándose para el lanzamiento!")
    time.sleep(1)  # Pausa de 1 segundo antes de comenzar la cuenta regresiva
    for i in range(inicio, -1, -1):
        if i == 0:
            print("¡Lanzamiento iniciado!")
        elif i % 5 == 0:
            print(f"Advertencia: {i} segundos para el lanzamiento")
            time.sleep(1)  # Pausa de 1 segundo entre cada número
        else:
            print(i)
            time.sleep(1)  # Pausa de 1 segundo entre cada número

inicio = int(input("Ingrese el valor inicial para la cuenta regresiva: "))

# Llamar a la función de cuenta regresiva con el valor proporcionado por el usuario
cuenta_regresiva(inicio)

