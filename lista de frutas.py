frutas = ["manzana", "naranja", "banana", "uva"]

"""
#primera fruta de la lista
print(frutas[0])

#última fruta de la lista
print(frutas[-1])

for i, fruta in enumerate(frutas, start=1):
  print(f"Posición {i}: {fruta}")
"""

frutas.append("fresa") #agregar
frutas.remove("uva") #eliminar

"""
print(len(frutas))
"""

print(frutas)

fruta_mas_larga = ""

while frutas:
  fruta = frutas.pop()
  if len(fruta) > len(fruta_mas_larga):
    fruta_mas_larga = fruta

print(f"Fruta con el nombre más largo: {fruta_mas_larga}")
print(f"Longitud del nombre: {len(fruta_mas_larga)}")
