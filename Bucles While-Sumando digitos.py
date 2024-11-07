n = int(input())
suma = 0
length = 0
while n!=0:
    length=n%10
    n//=10
    suma=suma+length

print(suma)