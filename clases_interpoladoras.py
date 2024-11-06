import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, expand, lambdify # Para trabajar con polinomios, variables simbólicas, expandir polinomios y convertirlos a funciones

class PolinomioInterpolador:
    def __init__(self):
        self.puntos = self.obtener_puntos()  # Solicitar puntos al usuario
        self.x = symbols('x')  # Variable simbólica para el polinomio
        self.polinomio = self.calcular_polinomio()  # Polinomio interpolador

    def obtener_puntos(self):
        puntos = []
        num_puntos = int(input("¿Cuántos puntos deseas ingresar? "))
        
        for i in range(num_puntos):
            x_val = float(input(f"Ingrese el valor de x{i+1}: "))
            y_val = float(input(f"Ingrese el valor de y{i+1}: "))
            puntos.append((x_val, y_val))
        
        return puntos

    def calcular_polinomio(self):
        n = len(self.puntos)
        polinomio = 0

        # Crear el polinomio de Lagrange
        for i in range(n):
            xi, yi = self.puntos[i] # Coordenadas del punto i
            termino = yi # Inicializar el término de Lagrange L_i(x)

            # Calcular el término de Lagrange L_i(x)
            for j in range(n):
                if i != j:
                    xj = self.puntos[j][0] # Coordenada x del punto j
                    termino *= (self.x - xj) / (xi - xj)

            polinomio += termino # Sumar el término de Lagrange al polinomio

        return expand(polinomio)

    def mostrar_polinomio(self):
        print("Polinomio interpolador:")
        print(self.polinomio)

    def evaluar(self, valor):
        resultado = self.polinomio.subs(self.x, valor) # Evaluar el polinomio en el valor dado
        print(f"P({valor}) = {resultado}")
        return resultado


interpolador = PolinomioInterpolador()
interpolador.mostrar_polinomio()

# Evaluar el polinomio en un punto
valor = float(input("Ingresa el valor en el que deseas evaluar el polinomio: "))
interpolador.evaluar(valor)

polinomio = interpolador.polinomio  # Polinomio interpolador
polinomio_func = lambdify(interpolador.x, polinomio, "numpy")  # Convertir a función numérica

# Valores para graficar
x_vals = np.linspace(1, 6, 100)
y_vals = polinomio_func(x_vals)

# Graficar los puntos y el polinomio
plt.scatter([1, 2, 3, 4, 5, 6], [3.5, 5.1, 6.8, 9.5, 11.2, 13.6], color="red", label="Datos")
plt.plot(x_vals, y_vals, label="Polinomio Interpolador", color="blue")
plt.xlabel("Semana")
plt.ylabel("Altura (cm)")
plt.legend()
plt.title("Interpolación del Crecimiento de una Planta")
plt.grid(True)
plt.show()