def calcular_edad(dia, mes, año):
  from datetime import date
  hoy = date.today()
  fecha_nacimiento = date(año, mes, dia)
  # Calcular diferencia de años
  años = hoy.year - fecha_nacimiento.year
  # Si el mes de nacimiento es mayor que el mes actual, restar un año
  if hoy.month < fecha_nacimiento.month:
    años -= 1
  # Si el día de nacimiento es mayor que el día actual, restar un mes al total de meses
  if hoy.day < fecha_nacimiento.day:
    meses = abs(11 - (fecha_nacimiento.month + hoy.month))
  else:
    meses = abs(hoy.month - fecha_nacimiento.month)
  # Calcular diferencia de días
  dias = abs(hoy.day - fecha_nacimiento.day)

  return f"Tu edad es de {años} años, {meses} meses y {dias} días."

dia = int(input("Introduce tu día de nacimiento: "))
mes = int(input("Introduce tu mes de nacimiento: "))
año = int(input("Introduce tu año de nacimiento: "))

edad = calcular_edad(dia, mes, año)
print(edad)
