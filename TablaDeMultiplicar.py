num=int(input("Escoge un numero: "))
for mult in [1,2,3,4,5,6,7,8,9,10]:
    print(str(num) + "x" + str(mult) + "=" + str(num*mult))

for mult in range(11):
    print(str(num) + "x" + str(mult) + "=" + str(num*mult))

for mult in range(1,11,2):
    print(str(num) + "x" + str(mult) + "=" + str(num*mult))