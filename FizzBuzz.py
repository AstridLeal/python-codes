# Toma una entrada n y saca los números de 1 a n
# Por cada múltiplo de 3, imprime "Solo" en lugar del número
# Por cada múltiplo de 5, imprime "Learn" en lugar del número
# Para los números que son múltiplos de 3 y 5, saca "SoloLearn"

n=int(input())

for x in range (1,n):
    if x%2!=0:
        if x%3==0 and x%5==0:
            print("SoloLearn")
            continue
        elif x%3==0:
            print("Solo")
            continue
        elif x%5==0:
            print("Learn")
            continue
        else:
            print(x)