from sympy import Matrix, symbols, simplify  # Para trabajar con matrices

class Matriz:
    def __init__(self, filas, columnas, id_matriz):
        self.filas = filas
        self.columnas = columnas
        self.id_matriz = id_matriz  # Identificador de la matriz
        self.matriz = self.crear_matriz()

    def crear_matriz(self):
        print(f"Ingresa los elementos de la matriz {self.id_matriz}, separados por espacios (puedes incluir números o variables)")
        matriz = []
        for i in range(self.filas):
            fila = input(f"Fila {i+1}: ").split()
            fila = [symbols(item) if not item.replace('.', '', 1).isdigit() else float(item) for item in fila]
            matriz.append(fila)
        return Matrix(matriz)

    def mostrar(self):
        print(f"Matriz {self.id_matriz}:")
        print(self.matriz)


    def __add__(self, otra):
        if self.filas != otra.filas or self.columnas != otra.columnas:
            print("Error: Las matrices deben tener el mismo tamaño para sumar.")
            return None
        suma = self.matriz + otra.matriz
        suma = suma.applyfunc(simplify) # Simplificar cada elemento de la matriz
        print("Suma de matrices:")
        print(suma)
        return suma

    def __sub__(self, otra):
        if self.filas != otra.filas or self.columnas != otra.columnas:
            print("Error: Las matrices deben tener el mismo tamaño para restar.")
            return None
        resta = self.matriz - otra.matriz
        resta = resta.applyfunc(simplify)
        print("Resta de matrices:")
        print(resta)
        return resta

    def __mul__(self, otra):
        if self.columnas != otra.filas:
            print("Error: El número de columnas de la primera matriz debe igualar el número de filas de la segunda para multiplicar.")
            return None
        producto = self.matriz * otra.matriz
        producto = producto.applyfunc(simplify)
        print("Producto de matrices:")
        print(producto)
        return producto

    def escalar(self, escalar):
        resultado = self.matriz * escalar
        resultado = resultado.applyfunc(simplify)
        print(f"Matriz {self.id_matriz} escalada por {escalar}:")
        print(resultado)
        return resultado

    def transponer(self):
        transpuesta = self.matriz.transpose()
        print(f"Matriz {self.id_matriz} transpuesta:")
        print(transpuesta)
        return transpuesta

    def tipo_matriz(self):
        # Verificar si la matriz es cuadrada
        if self.filas != self.columnas:
            print(f"La matriz {self.id_matriz} no es cuadrada, por lo tanto, no puede ser triangular ni diagonal.")
            return "Ninguna"
        
        es_triangular_superior = True
        es_triangular_inferior = True
        es_diagonal = True

        for i in range(self.filas):
            for j in range(self.columnas):
                valor_actual = simplify(self.matriz[i, j])

                # Usar `.is_zero` para verificar si el valor es cero después de simplificar
                if i > j and not valor_actual.is_zero:
                    es_triangular_superior = False
                if i < j and not valor_actual.is_zero:
                    es_triangular_inferior = False
                if i != j and not valor_actual.is_zero:
                    es_diagonal = False

        if es_diagonal:
            tipo = "Diagonal"
        elif es_triangular_superior:
            tipo = "Triangular superior"
        elif es_triangular_inferior:
            tipo = "Triangular inferior"
        else:
            tipo = "Ninguna"

        print(f"La matriz {self.id_matriz} es de tipo: {tipo}")
        return tipo

    def determinante(self, metodo="directo"):
        if self.filas != self.columnas:
            print(f"Error: La matriz {self.id_matriz} no es cuadrada, por lo tanto, no tiene determinante.")
            return None
        
        if metodo == "directo":
            det = self.matriz.det()
        elif metodo == "cofactores":
            det = self._determinante_por_cofactores(self.matriz)
        else:
            print("Método desconocido.")
            return None

        print(f"El determinante de la matriz {self.id_matriz} es: {det} (método: {metodo})")
        return det

    def _determinante_por_cofactores(self, matriz):
        if matriz.shape == (1, 1):
            return matriz[0, 0]
        elif matriz.shape == (2, 2):
            return matriz[0, 0] * matriz[1, 1] - matriz[0, 1] * matriz[1, 0]
        
        det = 0
        for j in range(matriz.shape[1]):
            cofactor = (-1) ** j * matriz[0, j] * self._determinante_por_cofactores(matriz.minor_submatrix(0, j))
            det += cofactor
        return simplify(det)

# Crear dos matrices a partir de la entrada del usuario
print("Definir primera matriz")
matriz1 = Matriz(3, 3, id_matriz="1")
matriz1.mostrar()

print("\nDefinir segunda matriz")
matriz2 = Matriz(3, 3, id_matriz="2")
matriz2.mostrar()

# Determinar el tipo de matriz
matriz1.tipo_matriz()
matriz2.tipo_matriz()

# Calcular determinantes usando ambos métodos
matriz1.determinante(metodo="directo")
matriz1.determinante(metodo="cofactores")
matriz2.determinante(metodo="directo")
matriz2.determinante(metodo="cofactores")

# Operaciones
suma = matriz1 + matriz2
resta = matriz1 - matriz2
producto = matriz1 * matriz2
matriz1.escalar(2)
matriz2.escalar(2)
matriz1.transponer()
matriz2.transponer()