import math

class Fraccion:
    def __init__(self, numerador, denominador):
        if denominador == 0:
            raise ValueError("El denominador no puede ser cero")
        self.numerador = numerador
        self.denominador = denominador
        self.simplificar()  # Simplificar la fracción al inicializar

    def simplificar(self):
        """Simplifica la fracción a su forma más simple."""
        gcd = math.gcd(self.numerador, self.denominador)
        self.numerador //= gcd
        self.denominador //= gcd

    def valor_decimal(self):
        """Devuelve el valor decimal aproximado de la fracción."""
        return self.numerador / self.denominador

    def __str__(self):
        """Representación de la fracción en formato 'numerador/denominador' y su valor decimal."""
        return f"{self.numerador}/{self.denominador} ≈ {self.valor_decimal():.2f}"

    def __eq__(self, otra):
        """Compara si dos fracciones son iguales."""
        if not isinstance(otra, Fraccion):
            return False
        return (self.numerador == otra.numerador and self.denominador == otra.denominador)

    def __add__(self, otra):
        """Suma dos fracciones."""
        if not isinstance(otra, Fraccion):
            raise ValueError("Solo se pueden sumar fracciones")
        # Calculamos el denominador común
        denominador_comun = self.denominador * otra.denominador
        numerador_sumado = (self.numerador * otra.denominador) + (otra.numerador * self.denominador)
        return Fraccion(numerador_sumado, denominador_comun)

# Ejemplo 
frac1 = Fraccion(2, 3)
frac2 = Fraccion(3, 4)
frac3 = Fraccion(5, 4)

print(frac1)  # Output: 2/3 ≈ 0.67
print(frac2)  # Output: 3/4 ≈ 0.75
print(frac3)  # Output: 5/4 ≈ 1.25
print(frac1 == frac3)  # Output: False
print(frac1 + frac2)  # Output: 17/12 ≈ 1.42
