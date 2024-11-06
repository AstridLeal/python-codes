class DimmerSwitch():
  def __init__(self, label):
    self.switchIsOn = False    # Indica si el interruptor está encendido o apagado
    self.brightness = 0        # Nivel de brillo actual
    self.label = label         # Etiqueta del interruptor

  def turnOn(self):
    self.switchIsOn = True     # Enciende el interruptor

  def turnOff(self):
    self.switchIsOn = False    # Apaga el interruptor

  def raiseLevel(self):
    if self.brightness < 10:
      self.brightness = self.brightness + 1    # Aumenta el nivel de brillo en 1

  def lowerLevel(self):
    if self.brightness > 0:
      self.brightness = self.brightness - 1    # Reduce el nivel de brillo en 1

  # Método adicional para depuración (debugging)
  def show(self):
    print(f'Interruptor {self.label}:')
    print('¿El interruptor está encendido?', self.switchIsOn)    # Muestra el estado del interruptor
    print('El nivel de brillo es:', self.brightness)    # Muestra el nivel de brillo actual

# Creamos tres objetos dimmer Switch
objeto_Dimmer1 = DimmerSwitch('Dimmer1')
print(type(objeto_Dimmer1))
print(objeto_Dimmer1)
print()
objeto_Dimmer2 = DimmerSwitch('Dimmer2')
print(type(objeto_Dimmer2))
print(objeto_Dimmer2)
print()
objeto_Dimmer3 = DimmerSwitch('Dimmer3')
print(type(objeto_Dimmer3))
print(objeto_Dimmer3)
print()