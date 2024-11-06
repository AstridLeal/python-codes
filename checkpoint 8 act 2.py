import random

numero_secreto = random.randint(1, 100)

intento = int(input("Introduce un número entre 1 y 100: "))

while intento != numero_secreto:
  if intento > numero_secreto:
    print("El número es menor.")
  else:
    print("El número es mayor.")

  intento = int(input("Introduce un número entre 1 y 100: "))

print("¡Felicidades! ¡Has adivinado el número secreto!")