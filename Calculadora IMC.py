# Formula peso entre la altura al cuadrado
# Underweight=menos de 18.5
# Normal=18.5-24.9
# Overweight=25-29.9
# Obesity=30 o mas

#peso en kg
#alura en metros

peso=float(input())
altura=float(input())
imc=peso/(altura**2)

if imc<18.5:
    print("Underweight")
elif imc>=18.5 and imc<=24.9:
    print("Normal")
elif imc>=25 and imc<=29.9:
    print("Overweight")
elif imc>=30:
    print("Obesity")