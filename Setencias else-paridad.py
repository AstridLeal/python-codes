# Escribe un programa que tome un número como entrada y
# -devuelve su doble si el número es par
# -devuelve su triple si el número es impar
# -devuelve 0 si el número es 0

num=int(input())

if num%2==0:
    print(num*2)
elif num == 0:
    print("0")
else:
    print(num*3)
