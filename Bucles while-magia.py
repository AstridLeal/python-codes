# Tienes una caja magica que duplica de objetos que metes cada dia.
# El programa dado toma como entrada el recuento inicial de los articulos y el numero de dias.
items = int(input())
days = int(input())

x=items*2
i=1
while i<days:
    i=i+1
    x=x+x

print(x)