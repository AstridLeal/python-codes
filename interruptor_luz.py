def turnOn():
  global switchIsOn
  # Prende las luces
  switchIsOn = True

def turnOff():
  global switchIsOn
  #apaga las luces
  switchIsOn = False

# Main code
switchIsOn = False # variable global booleana
  
# Test code
print(switchIsOn)
turnOn()
print(switchIsOn)
turnOff()
print(switchIsOn)
turnOn()
print(switchIsOn)