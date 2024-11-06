# Non-OOP
# Bank 2
# Single account
nombre_cuenta = ''
saldo_cuenta = 0
contrasenia_cuenta = ''

def nueva_cuenta(nombre, saldo, contrasenia):
  global nombre_cuenta, saldo_cuenta, contrasenia_cuenta 
  nombre_cuenta = nombre
  saldo_cuenta = saldo
  contrasenia_cuenta = contrasenia

def show():
  global nombre_cuenta, saldo_cuenta, contrasenia_cuenta
  print()
  print('--------------------------------------------')
  print('       Nombre', nombre_cuenta)
  print('       Saldo:', saldo_cuenta)
  print('       Contraseña:', contrasenia_cuenta)
  print('--------------------------------------------')
  print()

def obtener_saldo(contrasenia):
  global nombre_cuenta, saldo_cuenta, contrasenia_cuenta 
  if contrasenia != contrasenia_cuenta:
    print('Contraseña incorrecta')
    return None
  return saldo_cuenta

def deposito(cantidad_deposito, contrasenia):
  global nombre_cuenta, saldo_cuenta, contrasenia_cuenta
  if cantidad_deposito < 0:
      print('No puedes depositar una cantidad negativa!')
      return None
  if contrasenia != contrasenia_cuenta:
      print('Contraseña incorrecta')
      return None
  saldo_cuenta = saldo_cuenta + cantidad_deposito
  return saldo_cuenta


def retiro(amountToWithdraw, password):
  global nombre_cuenta, saldo_cuenta, contrasenia_cuenta 
  if amountToWithdraw < 0:
   print('No puedes retirar una cantidad negativa!')
   return None
  if password != contrasenia_cuenta:
    print('Contraseña incorrecta')
    return None
  if amountToWithdraw > saldo_cuenta:
    print('No tiene saldo suficiente')
    return None
  saldo_cuenta = saldo_cuenta - amountToWithdraw 
  return saldo_cuenta

nueva_cuenta("Joe", 100, 'soup')  # crea una cuenta

while True:
  print()
  print('Presiona b para obtener tu saldo') 
  print('Presiona d para hacer un deposito')
  print('Presiona w para hacer un retiro') 
  print('Presiona s para mostrar la cuenta') 
  print('Presiona q para salir')
  print()

  action = input('¿Qué te gustaría hacer? ') 
  action = action.lower()  # forzamos las minúsculas
  print()

  if action == 'b':
    print('Obtener saldo:')
    contrasenia_usuario = input('Por favor ingresa la contraseña: ')
    saldo = obtener_saldo(contrasenia_usuario)
    if saldo is not None:
        print('Tu saldo es:', saldo)
  elif action == 'd':
    print('Deposito:')
    cantidad_a_depositar = int(input('Por favor ingresa la cantidad a depositar: '))
    contrasenia_usuario = input('Por favor ingresa la contraseña: ')
    nuevo_saldo = deposito(cantidad_a_depositar, contrasenia_usuario) 
    if nuevo_saldo is not None:
      print('Tu nuevo saldo es:', nuevo_saldo)
  elif action == 'w':
    print('Retiro: ')
    cantidad_a_retirar = int(input('Por favor ingresa la cantidad a retirar: '))
    contrasenia_usuario = input('Por favor ingresa la contraseña: ')
    nuevo_saldo = retiro(cantidad_a_retirar, contrasenia_usuario)
    if nuevo_saldo is not None:
        print('Tu nuevo saldo es: ', nuevo_saldo)
  elif action == 's': 
    show()
  elif action == 'q':
    break

print('Bye')