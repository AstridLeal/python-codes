#Comprobador de pureza de oro que acepta solo el oro de 22K o 24K
#El oro de 22K tiene un 91,7% o más de oro
#El oro de 24K tiene un 99,9% de pureza

purity=float(input())

if purity>=91.7:
    print("Accepted")
