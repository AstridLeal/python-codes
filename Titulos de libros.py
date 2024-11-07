# Programa de categorización especial, que asigne a cada libro un código especial basado en su título:
# El código es igual a la primera letra del libro, seguido del número de caracteres del título.
# Por ejemplo, para "Harry Potter" sería H12 porque son 12 caracteres incluyendo el espacio.

i=0
while i<3:
  f=open("/Users/aslea/Documents/Phyton/booksnames.txt","r")
  cont=f.readlines()[i]
  y=len(cont)-1
  x=cont[0]
  print(x+str(y))
  i+=1
  f.close()

f=open("/Users/aslea/Documents/Phyton/booksnames.txt","r")

cont=f.readlines()[3]
y=len(cont)
x=cont[0]
print(x+str(y))

f.close()