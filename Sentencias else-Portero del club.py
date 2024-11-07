# Escribe un programa para controlar la entrada a un club.
# Sólo las personas mayores de 18 años pueden entrar al club.
# Tu programa toma la edad y el nombre de la persona para entrar, y saca "Bienvenido" seguido del nombre de la persona si se le permite entrar y
# "Lo siento" is es más joven que la edad permitida

edad=int(input())
nombre=input()

if edad>=18:
    print("Bienvenido "+nombre)
else:
    print("Lo siento")