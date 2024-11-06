# Definimos la clase Empleado que más adelante nos servirá como clase base

class Empleado():
  def __init__(self, nombre, puesto, sueldoPorHora=None):
      self.nombre = nombre
      self.puesto = puesto
      if sueldoPorHora is not None:
        sueldoPorHora = float(sueldoPorHora)
      self.sueldoPorHora = sueldoPorHora

  def obtenerNombre(self):
    return self.nombre

  def obtenerPuesto(self):
    return self.puesto

  def ingresoAnual(self):
    # 52 semanas * 5 días a la semana * 8 horas al día
    pago = 52 * 5 * 8 * self.sueldoPorHora
    return pago
  
# Definimos la clase Gerente que hereda de la clase Empleado

class Gerente(Empleado):
  def __init__(self, nombre, puesto, salario, listaDeReportes=None):
    self.salario = float(salario)
    if listaDeReportes is None:
      listaDeReportes = []
    self.listaDeReportes = listaDeReportes
    super().__init__(nombre,puesto) # llamamos a la función integrada super() que le pide a Python encontrar la clase base y llamar su método __init__()

  def obtenerReportes(self):
    return self.listaDeReportes

  def ingresoAnual(self, giveBonus = False):
    pago = self.salario
    if giveBonus:
        pago = pago + (0.1 * self.salario) # agregamos un bono del 10%
        print(self.nombre, 'obtiene un bono por su buen desempeño')
    return pago