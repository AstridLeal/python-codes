import matplotlib.pyplot as plt #funcion para trabajar como matlab
def generar_grafica_lineas(x, y):
  plt.plot(x, y)
  plt.xlabel("Eje X")
  plt.ylabel("Eje Y")
  plt.title("Gráfica de líneas")
  plt.show()

def generar_grafica_barras(x, y):
  plt.bar(x, y)
  plt.xlabel("Eje X")
  plt.ylabel("Eje Y")
  plt.title("Gráfica de barras")
  plt.show()

while True:
  print("1. Generar gráfica de líneas")
  print("2. Generar gráfica de barras")
  print("3. Salir")

  opcion = int(input("Elige una opción: "))

  if opcion == 1:
    x = [10, 20, 30, 40, 50]
    y = [22, 44, 66, 88, 110]
    generar_grafica_lineas(x, y)
  elif opcion == 2:
    x = ["A", "B", "C", "D", "E"]
    y = [10, 20, 30, 40, 50]
    generar_grafica_barras(x, y)
  elif opcion == 3:
    break
  else:
    print("Opción no válida.")
