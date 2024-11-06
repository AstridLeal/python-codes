numerador = input('Ingresa el numerador: ')
denominador = input('Ingresa el denominador: ')

try:
    # Convertir las entradas a enteros
    numerador = int(numerador)
    denominador = int(denominador)
    
    # Dividir los números
    resultado = numerador / denominador
    print('El resultado de la división es:', resultado)
    
except ZeroDivisionError:
    # Manejar la excepción de división por cero
    print('Error: No se puede dividir por cero.')
    
except ValueError:
    # Manejar la excepción de valor no entero
    print('Error: Entrada inválida. Por favor, ingresa números enteros.')
