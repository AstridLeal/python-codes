class Cuenta():
  # Constructor de la clase Cuenta
  def __init__(self, name, balance, password):
    self.name = name
    self.balance = int(balance)
    self.password = password

  # Método para depositar en la cuenta
  def deposit(self, amountToDeposit, password):
    if password != self.password:
      print('Lo siento, contraseña incorrecta')
      return None

    if amountToDeposit < 0:
      print('No puedes depositar una cantidad negativa')
      return None

    self.balance = self.balance + amountToDeposit
    return self.balance

  # Método para retirar dinero de la cuenta
  def withdraw(self, amountToWithdraw, password):
    if password != self.password:
      print('Contraseña incorrecta para esta cuenta')
      return None

    if amountToWithdraw < 0:
      print('No puedes retirar una cantidad negativa')
      return None

    if amountToWithdraw > self.balance:
      print('No puedes retirar más de lo que tienes en tu cuenta')
      return None

    self.balance = self.balance - amountToWithdraw
    return self.balance

  # Método para obtener el saldo de la cuenta
  def getBalance(self, password):
    if password != self.password:
      print('Lo siento, contraseña incorrecta')
      return None

    return self.balance

  # Agregado para depuración
  def show(self):
    print(' Nombre:', self.name)
    print(' Saldo:', self.balance)
    print(' Contraseña:', self.password)
    print()

# Programa de prueba usando cuentas
# Versión 2, utilizando una lista de cuentas
# Importar todo el código de la clase Cuenta desde el archivo Account.py

# Comenzar con una lista vacía de cuentas
listaDeCuentas = []

# Crear dos cuentas
objeto_Account = Cuenta('Joe', 100, 'ContraseñaDeJoe')
listaDeCuentas.append(objeto_Account)
print("El número de cuenta de Joe es 0")

objeto_Account = Cuenta('Mary', 12345, 'ContraseñaDeMary')
listaDeCuentas.append(objeto_Account)
print("El número de cuenta de Mary es 1")

listaDeCuentas[0].show()
listaDeCuentas[1].show()
print()

# Llamar a algunos métodos de las cuentas diferentes
print('Llamando a métodos de las dos cuentas...')
listaDeCuentas[0].deposit(50, 'ContraseñaDeJoe')
listaDeCuentas[1].withdraw(345, 'ContraseñaDeMary')
listaDeCuentas[1].deposit(100, 'ContraseñaDeMary')

# Mostrar las cuentas
listaDeCuentas[0].show()
listaDeCuentas[1].show()

# Crear otra cuenta con información proporcionada por el usuario
print()
nombreUsuario = input('¿Cuál es el nombre para la nueva cuenta de usuario? ')
saldoUsuario = int(input('¿Cuál es el saldo inicial para esta cuenta? '))
passUsuario = input('¿Cuál es la contraseña que deseas utilizar para esta cuenta? ')
objeto_Account = Cuenta(nombreUsuario, saldoUsuario, passUsuario)
listaDeCuentas.append(objeto_Account)  # agregar a la lista de cuentas

# Mostrar la nueva cuenta de usuario creada
print('Se ha creado una nueva cuenta, el número de cuenta es 2')
listaDeCuentas[2].show()

# Realicemos un depósito de 100 en la nueva cuenta
listaDeCuentas[2].deposit(100, passUsuario)
saldoUsuario = listaDeCuentas[2].getBalance(passUsuario)
print()
print('Después de depositar 100, el saldo del usuario es:', saldoUsuario)

# Mostrar la nueva cuenta de usuario
listaDeCuentas[2].show()