# Se te da un programa con dos entradas: una como contraseña y la segunda como repetición de la contraseña.
# Completa y llama a la función dada para salir "Correcto" si la contraseña y la repetición son iguales, y salir "Incorrecto", si no lo son.

password=input()
repeat=input()

def validate(text1, text2):
    if password==repeat:
        print("Correct")
    else:
        print("Wrong")

validate(password,repeat)