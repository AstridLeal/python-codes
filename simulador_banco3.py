# Non-OOP
# Bank 3
# Two accounts
nombre_cuenta_0 = ''
saldo_cuenta_0 = 0
contrasenia_cuenta_0 = ''

nombre_cuenta_1 = ''
saldo_cuenta_1 = 0
contrasenia_cuenta_1 = ''

nCuentas = 0

def nueva_cuenta(numero_de_cuenta, nombre, saldo, contrasenia):
  global nombre_cuenta_0, saldo_cuenta_0, contrasenia_cuenta_0 
  global nombre_cuenta_1, saldo_cuenta_1, contrasenia_cuenta_1
  if numero_de_cuenta == 0:
    nombre_cuenta_0 = nombre
    saldo_cuenta_0 = saldo
    contrasenia_cuenta_0 = contrasenia
  if numero_de_cuenta == 1:
    nombre_cuenta_1 = nombre
    saldo_cuenta_1 = saldo
    contrasenia_cuenta_1 = contrasenia

def show():
  global nombre_cuenta_0, saldo_cuenta_0, contrasenia_cuenta_0
  global nombre_cuenta_1, saldo_cuenta_1, contrasenia_cuenta_1 
  if nombre_cuenta_0 != '':
    print('Cuenta 0')
    print('--------------------------------------------')
    print('       nombre', nombre_cuenta_0)
    print('       saldo:', saldo_cuenta_0)
    print('       contraseña:', contrasenia_cuenta_0)
    print('--------------------------------------------')
    print()
  if nombre_cuenta_1 != '':
      print('Cuenta 1')
      print('--------------------------------------------')
      print('       nombre', nombre_cuenta_1)
      print('       saldo:', saldo_cuenta_1)
      print('       contraseña:', contrasenia_cuenta_1)
      print('--------------------------------------------')
      print()

def getsaldo(numero_de_cuenta, contrasenia):
  global nombre_cuenta_0, saldo_cuenta_0, contrasenia_cuenta_0 
  global nombre_cuenta_1, saldo_cuenta_1, contrasenia_cuenta_1
  if numero_de_cuenta == 0:
      if contrasenia != contrasenia_cuenta_0:
          print('Contraseña incorrecta')
          return None
      return saldo_cuenta_0
  if numero_de_cuenta == 1:
      if contrasenia != contrasenia_cuenta_1:
          print('Contraseña incorrecta')
          return None
      return saldo_cuenta_1

def deposito(numero_de_cuenta, cantidad_deposito, contrasenia):
    global saldo_cuenta_0, saldo_cuenta_1
    if cantidad_deposito < 0:
        print('No puedes depositar una cantidad negativa!')
        return None
    if numero_de_cuenta == 0:
        if contrasenia != contrasenia_cuenta_0:
            print('Contraseña incorrecta')
            return None
        saldo_cuenta_0 = saldo_cuenta_0 + cantidad_deposito
        return saldo_cuenta_0
    elif numero_de_cuenta == 1:
        if contrasenia != contrasenia_cuenta_1:
            print('Contraseña incorrecta')
            return None
        saldo_cuenta_1 = saldo_cuenta_1 + cantidad_deposito
        return saldo_cuenta_1

def retiro(numero_de_cuenta, amountToWithdraw, password):
    global saldo_cuenta_0, saldo_cuenta_1
    if amountToWithdraw < 0:
        print('No puedes retirar una cantidad negativa!')
        return None
    if numero_de_cuenta == 0:
        if password != contrasenia_cuenta_0:
            print('Contraseña incorrecta')
            return None
        if amountToWithdraw > saldo_cuenta_0:
            print('No tiene saldo suficiente')
            return None
        saldo_cuenta_0 = saldo_cuenta_0 - amountToWithdraw 
        return saldo_cuenta_0
    elif numero_de_cuenta == 1:
        if password != contrasenia_cuenta_1:
            print('Contraseña incorrecta')
            return None
        if amountToWithdraw > saldo_cuenta_1:
            print('No tiene saldo suficiente')
            return None
        saldo_cuenta_1 = saldo_cuenta_1 - amountToWithdraw 
        return saldo_cuenta_1

nueva_cuenta(0, "Astrid", 100, 'hamster')  # crea la cuenta 0
nueva_cuenta(1, "Reyes", 200, 'perro')  # crea la cuenta 1

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
        numero_de_cuenta = int(input('Por favor ingresa el número de cuenta (0 o 1): '))
        contrasenia_usuario = input('Por favor ingresa la contraseña: ')
        saldo = getsaldo(numero_de_cuenta, contrasenia_usuario)
        if saldo is not None:
            print('Tu saldo es:', saldo)
    elif action == 'd':
        print('Deposito:')
        numero_de_cuenta = int(input('Por favor ingresa el número de cuenta (0 o 1): '))
        cantidad_a_depositar = int(input('Por favor ingresa la cantidad a depositar: '))
        contrasenia_usuario = input('Por favor ingresa la contraseña: ')
        nuevo_saldo = deposito(numero_de_cuenta, cantidad_a_depositar, contrasenia_usuario) 
        if nuevo_saldo is not None:
            print('Tu nuevo saldo es:', nuevo_saldo)
    elif action == 'w':
        print('Retiro:')
        numero_de_cuenta = int(input('Por favor ingresa el número de cuenta (0 o 1): '))
        cantidad_a_retirar = int(input('Por favor ingresa la cantidad a retirar: '))
        contrasenia_usuario = input('Por favor ingresa la contraseña: ')
        nuevo_saldo = retiro(numero_de_cuenta, cantidad_a_retirar, contrasenia_usuario)
        if nuevo_saldo is not None:
            print('Tu nuevo saldo es:', nuevo_saldo)
    elif action == 's': 
        show()
    elif action == 'q':
        break

print('Bye')