# Dada la edad de una persona como entrada, es necesario dar salida a su grupo de edad.
# Niño: 0 a 11
# Adolescente: 12 a 17
# Adulto: 18 a 64
# Anciano: 65+

age=int(input())
if age>=0 and age<=11:
    print("Child")
elif age>=12 and age<=17:
    print("Teen")
elif age>=18 and age<=64:
    print("Adult")
else:
    print("Senior")