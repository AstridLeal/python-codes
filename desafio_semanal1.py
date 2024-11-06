# Crea un programa que reciba una inecuación lineal por parte del usuario y devuelva su conjunto solución, sin utilizar librerías.
# Fecha Límite: Viernes antes de las 2:00 pm hora CDMX
# Envío: Enviar el programa a cualquier tutor antes de la fecha y hora límite. ( Raúl Baltazar Domínguez Sahori Solana Diego Preza José Esteva )

# Es importante tener en cuenta que este ejemplo es bastante básico y solo maneja inecuaciones en la forma 
# ax + b <= c, 
# ax + b >= c, 
# ax + b < c, 
# ax + b > c y sus equivalentes simplificados (ej. ax <= c).

def parse_inequation(inequation):
    # Remover espacios en blanco
    inequation = inequation.replace(" ", "")
    
    # Identificar el signo de la inecuación
    if '<=' in inequation:
        parts = inequation.split('<=')
        operator = '<='
    elif '>=' in inequation:
        parts = inequation.split('>=')
        operator = '>='
    elif '<' in inequation:
        parts = inequation.split('<')
        operator = '<'
    elif '>' in inequation:
        parts = inequation.split('>')
        operator = '>'
    else:
        raise ValueError("Inecuación no válida")
    
    # Separar las partes de la inecuación
    left = parts[0]
    right = parts[1]
    
    # Obtener el coeficiente y la constante
    if 'x' in left:
        left_parts = left.split('x')
        coefficient = float(left_parts[0]) if left_parts[0] != '' else 1.0
        constant = -float(right)
    else:
        left_parts = right.split('x')
        coefficient = -float(left_parts[0]) if left_parts[0] != '' else -1.0
        constant = -float(left)
    
    return coefficient, constant, operator

def solve_inequation(coefficient, constant, operator):
    if coefficient == 0:
        if operator in ['<=', '<']:
            if constant >= 0:
                return "Solución: Todos los números reales"
            else:
                return "Solución: No hay solución"
        elif operator in ['>=', '>']:
            if constant <= 0:
                return "Solución: Todos los números reales"
            else:
                return "Solución: No hay solución"
    
    # Resolver la inecuación
    threshold = -constant / coefficient
    if operator == '<=':
        return f"Solución: x <= {threshold}"
    elif operator == '>=':
        return f"Solución: x >= {threshold}"
    elif operator == '<':
        return f"Solución: x < {threshold}"
    elif operator == '>':
        return f"Solución: x > {threshold}"

def main():
    # Leer la inecuación desde la entrada del usuario
    inequation = input("Introduce una inecuación lineal (ej. '3x + 4 <= 7'): ")
    
    try:
        # Parsear la inecuación
        coefficient, constant, operator = parse_inequation(inequation)
        
        # Resolver la inecuación
        solution = solve_inequation(coefficient, constant, operator)
        
        # Imprimir el resultado
        print(solution)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
