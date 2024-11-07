# El teorema de Pitágoras dice:
# En un triángulo en ángulo recto, el cuadrado del lado de la hipotenusa es igual a la suma de los cuadrados de los otros dos lados.

# Escribe un programa que tome las longitudes de los lados de los triángulos como entradas y salidas, tanto si nuestro triángulo es recto como si no.
# Si el triángulo es recto, el programa debería dar como resultado "En ángulo recto", y "No en ángulo recto" si no lo es.

lado1=int(input())
lado2=int(input())
lado3=int(input())

suma=(lado1**2)+(lado2**2)
hipo=(lado3**2)

if suma==hipo:
    print("Right-angled")
else:
    print("Not right-angled")

