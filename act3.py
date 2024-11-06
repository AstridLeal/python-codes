#Crea un programa que pida al usuario que introduzca una cadena de texto y luego imprima la primera y última letra de la cadena.

cadena = input("Ingresa una cadena de texto: ")

primer_letra = cadena[0]
ultima_letra = cadena [-1] #negativo porque es la última letra de la cadena y se posiciona en -1

print(f"Primera letra: {primer_letra}")
print(f"Última letra: {ultima_letra}")
