numero_inicial = int(input("Introduce el número entero inicial: "))
numero_final = int(input("Introduce el número entero final: "))

for numero in range(numero_inicial, numero_final + 1):
  if numero % 2 != 0:
    print(numero)