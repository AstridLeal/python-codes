class Cuenta():
  def __init__(self, nombre, saldo, password):
    self.name = nombre
    self.balance = float(saldo)
    self.password = password

  def deposito(self, cantidad_a_depositar, password):
    if password != self.password:
      print('Contraseña incorrecta')
      return None
    if cantidad_a_depositar < 0:
      print('No puedes depositar un monto negativo')
      return None

    self.balance = self.balance + cantidad_a_depositar
    return self.balance

  def retiro(self, cantidad_a_retirar, password):
    if password != self.password:
      print('Contraseña incorrecta')
      return None
    if cantidad_a_retirar < 0:
      print('No puedes retirar un monto negativo')
      return None
    if cantidad_a_retirar > self.balance:
      print('Saldo insuficiente')
      return None

    self.balance = self.balance - cantidad_a_retirar
    return self.balance

  def obtener_saldo(self, password):
    if password != self.password:
      print('Contraseña incorrecta')
      return None
    return self.balance

  # Added for debugging
  def show(self):
    print('       Nombre:', self.name)
    print('       Saldo:', self.balance)
    print('       Contraseña:', self.password)
    print()


# Crear una cuenta
mi_cuenta = Cuenta("Joe", 500, "soup")

# Mostrar información de la cuenta
mi_cuenta.show()

# Depositar en la cuenta
nuevo_saldo = mi_cuenta.deposito(100, "soup")
print("Nuevo saldo:", nuevo_saldo)

# Retirar de la cuenta
nuevo_saldo = mi_cuenta.retiro(50, "soup")
print("Nuevo saldo:", nuevo_saldo)

# Obtener el saldo de la cuenta
saldo_actual = mi_cuenta.obtener_saldo("soup")
print("Saldo actual:", saldo_actual)