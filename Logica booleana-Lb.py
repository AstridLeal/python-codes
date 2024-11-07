# Necesitas crear un programa que muestre si una tienda est[a abierta o cerrada, basado en la hora y el d[ia de la semana.
# La tienda esta abierta todos los dias de 10 a 21, excepto el sabado y el domingo.
# Necesitas tomar la hora y el dia de la semana como entrada
# El dia de la semana se representa como un entero (1 para el lunes, 2 para el martes, etc.)

hour=int(input())
day=int(input())

if hour>=10 and hour<=21 and day>=1 and day<=5:
    print("Abierto")
else:
    print("Cerrado")