class LightSwitch():
  def __init__(self):
    self.switchIsOn = False
  def turnOn(self):
    # Enciende el switch
    self.switchIsOn = True
  def turnOff(self):
    # Apaga el switch
    self.switchIsOn = False
  def show(self):  # Agregamos un método para mostrar el estado
    print(self.switchIsOn)

# Main code
objeto_LightSwitch = LightSwitch()  # Creamos un objeto del tipo LigthSwitch

# Llamamos el método Show
objeto_LightSwitch.show()
objeto_LightSwitch.turnOn()
objeto_LightSwitch.show()
objeto_LightSwitch.turnOff()
objeto_LightSwitch.show()
objeto_LightSwitch.turnOn()
objeto_LightSwitch.show()