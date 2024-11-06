def encontrar_mayor_menor(a, b, c):
  mayor = max(a, b, c)
  menor = min(a, b, c)
  return mayor, menor

a = int(input("Introduce el primer número entero: "))
b = int(input("Introduce el segundo número entero: "))
c = int(input("Introduce el tercer número entero: "))

mayor, menor = encontrar_mayor_menor(a, b, c)

print(f"El número mayor es {mayor}")
print(f"El número menor es {menor}")
