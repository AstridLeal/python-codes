def generar_primos(n):
  primos = []
  candidato = 2

  while len(primos) < n:
    #Comprueba si el candidato es primo (solo se puede dividir por si mismo)
    es_primo = True
    for divisor in primos:
      if candidato % divisor == 0:
        es_primo = False
        break

    #Si el candidato es primo, lo agrega a la lista
    if es_primo:
      primos.append(candidato)

    candidato += 1
  return primos

n=int(input("Ingrese un número entero: "))
numero_primos = generar_primos(n)
print("Los primeros", n, "números primos son:",numero_primos)


