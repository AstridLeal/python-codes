def multiplicar(a, b):
  producto = 0
  for i in range(b):
    producto += a

  return producto

a = int(input("Introduce el primer número entero: "))
b = int(input("Introduce el segundo número entero: "))

resultado = multiplicar(a, b)

print("El resultado de multiplicar ", a, "y", b, "es:", resultado)
