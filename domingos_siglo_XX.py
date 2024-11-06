'''
Desafio Semanal 3 - Problema 3
Se te da la siguiente información, pero puedes preferir investigar por tu cuenta:
- El 1 de enero de 1900 fue un lunes.
- Treinta días tiene septiembre,
abril, junio y noviembre.
Todos los demás tienen treinta y uno,
excepto febrero,
que tiene veintiocho, llueva o truene.
Y en años bisiestos, veintinueve.
- Un año bisiesto ocurre en cualquier año divisible por 4, pero no en un siglo a menos que sea divisible por 400.
¿Cuántos domingos cayeron el primer día del mes durante el siglo XX (del 1 de enero de 1901 al 31 de diciembre de 2000)?
'''

def es_bisiesto(ano):
    # determina si un año es bisiesto.
    # un año es bisiesto si es divisible por 4, excepto los años que son divisibles por 100 a menos que también sean divisibles por 400
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# número de días en cada mes de un año no bisiesto
dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# día de la semana del primer día del mes
# (1 de enero de 1900 fue lunes, así que 365 días después es martes)
dia_semana = 1  # 0: domingo, 1: lunes, ..., 6: sábado

# contador de domingos en el primer día del mes
domingos_primer_dia = 0

# iteramos sobre los años del siglo XX
for ano in range(1901, 2001):
    for mes in range(12):
        if dia_semana == 0:  # Domingo
            domingos_primer_dia += 1
        # Actualizamos el día de la semana para el primer día del próximo mes
        if mes == 1 and es_bisiesto(ano): # checa si es febrero y es un año bisiesto
            dia_semana = (dia_semana + 29) % 7 
            # añade 29 días al día de la semana actual porque en un año bisiesto, febrero tiene 29 días
            # usamos "%7" para asegurar que dia_semana se mantenga entre 0 y 6
        else:
            dia_semana = (dia_semana + dias_mes[mes]) % 7
            # calcula el día de la semana del primer día del mes siguiente, teniendo en cuenta el número de días del mes actual

print("Número de domingos que cayeron el primer día del mes durante el siglo XX:", domingos_primer_dia)