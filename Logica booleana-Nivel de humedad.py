# La humedad relativa confortable para el ser humano est[a entre el 40% y el 60%
# El programa dado toma el porcentaje de humedad como entrada.

# Tarea: Completar el codigo para generar "norm" si el porcentaje de humedad tomado esta en el rango de 40 y 60 inclusive. No generes nada de lo contrario.


h=int(input())

print("{pronoun}".format(pronoun="norm" if (h>40 and h<60) else " "))
