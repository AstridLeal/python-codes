def poor_mans_bar_chart():
    texto = input("Ingresa tu texto: ")
    
    #diccionario para almacenar la frecuencia de cada vocal
    frecuencia_vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    #Contar la frecuencia de cada vocal
    for letra in texto.lower():
        if letra in frecuencia_vocales:
            frecuencia_vocales[letra] += 1
    
    vocales_ordenadas = sorted(frecuencia_vocales.keys())
    
    max_frecuencia = max(frecuencia_vocales.values())
    
    #Gráfico de barras
    for i in range(max_frecuencia, 0, -1):
        line = ''
        for vocal in vocales_ordenadas:
            if frecuencia_vocales[vocal] >= i:
                line += '# '
            else:
                line += '  '
        print(line)
    
    print(' '.join(vocales_ordenadas))

poor_mans_bar_chart()
