texto = input("Ingrese un texto: ")

suma_ascii = 0

for caracter in texto:
    # Obtener el valor ASCII del carácter actual y sumarlo a la suma total
    valor_ascii = ord(caracter) #se usa la funcion ord() para obtener el valor ASCII para cada caracter
    suma_ascii += valor_ascii

print("La suma total de los valores ASCII en el texto es:", suma_ascii)


