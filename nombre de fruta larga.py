frutas = ["manzana", "naranja", "banana", "fresa"]
print(frutas)

fruta_mas_larga = ""
longitud_fruta_mas_larga = 0

indice = 0

while indice < len(frutas):
    fruta_actual = frutas[indice]
    
    if len(fruta_actual) > longitud_fruta_mas_larga:
        fruta_mas_larga = fruta_actual
        longitud_fruta_mas_larga = len(fruta_actual)
    
    indice += 1

print("La fruta más larga es:", fruta_mas_larga)
print("La cantidad de caracteres en el nombre es:", longitud_fruta_mas_larga)