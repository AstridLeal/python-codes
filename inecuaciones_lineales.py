import sympy as sp # Para resolver inecuaciones
import matplotlib.pyplot as plt # Para graficar intervalos

"""
Sirve para ecuaciones como:
3*(x + 1) < 2*x + 4 <= 6
5 - 2*x < 1 + 3*x <= 10
3*x - 5 < 2*x + 4 <= 3*x + 2
-2*x + 5 < 7 - x <= 2*(x - 3)
"""

def resolver_inecuaciones(expr):
    # Definir la variable
    x = sp.symbols('x')
    
    # Dividimos la expresión en dos partes: "<" y "<="
    # Reemplazamos todos los "<=" por "<" para un manejo unificado
    inecuaciones = expr.split("<=")
    
    # Tomamos las partes iniciales y las dividimos por el signo "<"
    sub_inecuaciones = inecuaciones[0].split("<")
    
    # Creamos las expresiones de las inecuaciones
    ineq1 = sp.sympify(sub_inecuaciones[0]) < sp.sympify(sub_inecuaciones[1]) # Inecuación 1
    ineq2 = sp.sympify(sub_inecuaciones[1]) <= sp.sympify(inecuaciones[1]) # Inecuación 2
    
    # Resolvemos ambas inecuaciones
    sol1 = sp.solve_univariate_inequality(ineq1, x, relational=False)
    sol2 = sp.solve_univariate_inequality(ineq2, x, relational=False)
    
    # Intersección de las soluciones
    solucion_final = sol1.intersect(sol2)
    
    # Mostrar la solución como intervalo
    print(f"La solución de la inecuación {expr} es: {solucion_final}")
    
    # Convertir el intervalo en formato visual
    graficar_intervalo(solucion_final)

def graficar_intervalo(intervalo):
    # Dibujar la recta numérica para representar el intervalo
    fig, ax = plt.subplots()

    # Generar la recta numérica básica
    ax.plot(range(-10, 11), [0]*21, color='black')  # Eje x

    # Definir los límites del intervalo
    if intervalo.start.is_infinite:
        start = -10  # Si el inicio es infinito, dibujamos desde -10
    else:
        start = int(intervalo.start)

    if intervalo.end.is_infinite:
        end = 10  # Si el final es infinito, dibujamos hasta 10
    else:
        end = int(intervalo.end)

    # Dibujar la representación del intervalo
    if intervalo.left_open:  # Si el límite izquierdo es abierto
        ax.plot(start, 0, marker='o', color='white', markeredgecolor='black', markersize=10)
    else:  # Si el límite izquierdo es cerrado
        ax.plot(start, 0, marker='o', color='black', markersize=10)

    if intervalo.right_open:  # Si el límite derecho es abierto
        ax.plot(end, 0, marker='o', color='white', markeredgecolor='black', markersize=10)
    else:  # Si el límite derecho es cerrado
        ax.plot(end, 0, marker='o', color='black', markersize=10)

    # Rellenar el intervalo
    ax.plot(range(start + 1, end), [0]*(end-start-1), color='blue', linewidth=4)
    
    # Etiquetas y límites
    ax.set_xlim(-10, 10) # Limitar el eje x
    ax.set_ylim(-1, 1) # Limitar el eje y
    ax.set_yticks([])  # Eliminar el eje y

    plt.show()

if __name__ == "__main__":
    # Solicitar al usuario que ingrese una inecuación lineal
    expresion_usuario = input("Introduce la inecuación lineal: ")
    resolver_inecuaciones(expresion_usuario)