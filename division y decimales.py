def convertir_a_decimal(numerador, denominador):
    #divide el numerador por el denominador y redondea el resultado a 4 decimales
  return round(numerador / denominador, 4)

numerador = int(input("Introduce el numerador de la fracción: "))
denominador = int(input("Introduce el denominador de la fracción: "))

decimal = convertir_a_decimal(numerador, denominador)

print("La fracción", numerador, "/" ,denominador, "es aproximadamente", decimal)
