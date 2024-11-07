# Imagina una maquina expendedora que vende frutas.
# Cada fruta tiene su propio numero, empezando por el 0.
# Escribe un programa para que la maquina expendedora, que tomara un numero n como entrada del cliente y devolvera la fruta con ese indice.

frutas=["manzana","cereza","banana","kiwi","limon","pera","melocoton","aguacate"]

num=int(input())

if num<0 or num>7:
    print("Numero equivocado")

if num==0:
    print(frutas[0])
elif num==1:
    print(frutas[1])
elif num==2:
    print(frutas[2])
elif num==3:
    print(frutas[3])
elif num==4:
    print(frutas[4])
elif num==5:
    print(frutas[5])
elif num==6:
    print(frutas[6])
elif num==7:
    print(frutas[7])

