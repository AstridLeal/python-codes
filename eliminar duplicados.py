def eliminar_duplicados(lista):
  unicos = []
  i = 0

  while i < len(lista):
    actual = lista[i]

    #Bucle 'for' para buscar duplicados del elemento actual
    duplicado = False
    for j in range(i + 1, len(lista)):
      if lista[j] == actual:
        duplicado = True
        break

    #Si el elemento actual no es un duplicado, se agrega a la lista 'unicos'
    if not duplicado:
      unicos.append(actual)
    i += 1
  return unicos

numeros = [1, 2, 3, 1, 2, 4, 5, 3, 5]
print(numeros)
numeros_sin_duplicados = eliminar_duplicados(numeros)
print(numeros_sin_duplicados)
