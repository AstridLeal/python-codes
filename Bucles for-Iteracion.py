# Dada una lista de numeros, saca su suma
list=[1,2,3,4,5,6,7,8,9]
sum=0
x=0
for num in list:
    x=num%10
    num//=10
    sum = sum + x
print(sum)