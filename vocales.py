#diccionario de vocales 
vocales = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

#convertir el texto a minúsculas
texto = input("Introduce un texto: ").lower()

#bucle que recorre el texto para contar cada vocal que aparece en el texto
for caracter in texto:
    if caracter in vocales:
        vocales[caracter] += 1

#imprime los resultados
for vocal, frecuencia in vocales.items():
    print(f"Vocal {vocal}: {frecuencia}")
    
