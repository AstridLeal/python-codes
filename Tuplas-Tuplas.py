# Se te dan las coordenadas de 2 puntos y necesitas encontrar la distancia en línea recta entre ellos
# Las coordenadas se proporcionan en una tupla
# La distancia lineal es la raíz cuadrada del cuadrado de la distancia horizontal + el cuadrado de la distancia vertical entre dos puntos
# El primer valor representa la coordenada x, mientras que el segundo valor representa la coordenada y del punto p

import math

p1=(23,-88)
p2=(6,42)
x=(p1[0]-p2[0])**2
y=(p1[1]-p2[1])**2
z=x+y
d=math.sqrt(z)
print(d)