#Calculadora que suma multiples numeros hasta que introduzcas "stop"

sum=0
while True:
    x=int(input())
    sum=sum+x
    if x=="stop":
        print(sum)
        break