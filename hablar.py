# 3 clases, cada una con un método "hablar"

class Perro():
  def __init__ (self, nombre):
    self.nombre=nombre

  def hablar(self):
      print (self.nombre, 'dice ¡guau, guau, guau!')

class Gato():
  def __init__ (self, nombre):
    self.nombre=nombre

  def hablar(self):
      print (self.nombre, 'dice miaaaauu')

class Pollo():
  def __init__ (self, nombre):
    self.nombre=nombre

  def hablar(self):
      print (self.nombre, 'dice pio pio')


perro1=Perro('Rover')
perro2=Perro('Fido')
gato1=Gato('Fluffy')
gato2=Gato('Spike')
pollo1=Pollo('Abelardo')

listaMascotas=[perro1, perro2, gato1, gato2, pollo1]

# Enviamos el mismo mensaje (llamamos al mismo método) a cada mascota.
for mascota in listaMascotas:
  mascota.hablar()