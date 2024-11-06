from sympy import symbols, Poly # Para trabajar con polinomios
import numpy as np # Para crear y operar polinomios de forma sencilla

def ingresar_polinomio():
    # Solicita al usuario que ingrese los coeficientes separados por espacios
    print("Introduce los coeficientes del polinomio, empezando por el término de mayor grado, separados por espacios: ")
    coeficientes = input("Por ejemplo, para 1x^2 + 3x - 5, introduce '1 3 -5': ")
    # Convierte los coeficientes en una lista (permite letras para coeficientes simbólicos)
    coeficientes = [eval(c) for c in coeficientes.split()]
    return coeficientes

def suma_polinomios_manual(p1, p2):
    # Ajustamos los polinomios a la misma longitud con coeficientes de cero
    grado_max = max(len(p1), len(p2)) # Grado máximo de los polinomios
    p1 = [0] * (grado_max - len(p1)) + p1 # Añadimos ceros al inicio
    p2 = [0] * (grado_max - len(p2)) + p2 
    # Sumamos coeficiente a coeficiente
    suma = [p1[i] + p2[i] for i in range(grado_max)]
    return suma

def suma_polinomios_sympy(p1, p2):
    # Definimos la variable simbólica x
    x = symbols('x')
    # Creamos polinomios usando SymPy
    polinomio1 = Poly.from_list(p1, x) # Convertimos la lista de coeficientes en un polinomio
    polinomio2 = Poly.from_list(p2, x)
    # Sumamos los polinomios simbólicamente
    suma = polinomio1 + polinomio2
    return suma

# Solicitar al usuario que ingrese los polinomios
print("Introduce el primer polinomio:")
p1 = ingresar_polinomio()

print("Introduce el segundo polinomio:")
p2 = ingresar_polinomio()

# Suma de polinomios manual
suma_manual = suma_polinomios_manual(p1, p2)
print("Suma manual de coeficientes:", suma_manual)

# Suma de polinomios con SymPy
suma_sympy = suma_polinomios_sympy(p1, p2)
print("Suma con SymPy:", suma_sympy)

# Comprobación de resultados
print("¿Es el resultado el mismo?", suma_sympy.as_list() == suma_manual)