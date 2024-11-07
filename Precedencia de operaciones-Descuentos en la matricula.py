# La Universidad ofrece a los estudiantes descuentos en la matricula dependiendo de su rendimiento
# 90-100 => 50%
# 80-89 => 30%
# 70-79 => 10%
# 0-69 => 0%
# Escribe un programa que tome las puntuaciones del primer y segundo semestre, luego calcula el promedio de puntuacion y da el resultado, dependiendo de la puntuacion

cal1=int(input())
cal2=int(input())

prom=(cal1+cal2)/2

if prom>=90 and prom<=100:
    print("50")
elif prom>=80 and prom<=89:
    print("30")
elif prom>=70 and prom<=79:
    print("10")
elif prom>=0 and prom<=69:
    print("0")