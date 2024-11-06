from Account import Cuenta

diccionario_cuentas = {}

nextAccountNumber = 1

while True:
    print()
    print('Presiona b para obtener el saldo')
    print('Presiona d para hacer un depósito')
    print('Presiona o para abrir una nueva cuenta')
    print('Presiona w para hacer un retiro')
    print('Presiona s para mostrar todas las cuentas')
    print('Presiona q para salir')
    print()
    accion = input('¿Qué deseas hacer? ')
    accion = accion.lower()
    print()

    if accion == 'b':
        print('*** Obtener Saldo ***')
        numeroCuentaUsuario = int(input('Por favor, ingresa el número de tu cuenta: '))
        passCuentaUsuario = input('Por favor, ingresa la contraseña: ')
        if numeroCuentaUsuario in diccionario_cuentas:
            objeto_Cuenta = diccionario_cuentas[numeroCuentaUsuario]
            saldoActual = objeto_Cuenta.getBalance(passCuentaUsuario)
            if saldoActual is not None:
                print('Tu saldo es:', saldoActual)
        else:
            print('Número de cuenta no encontrado')

    elif accion == 'd':
        print('*** Depósito ***')
        numeroCuentaUsuario = int(input('Por favor, ingresa el número de cuenta: '))
        montoDepositoUsuario = int(input('Por favor, ingresa la cantidad a depositar: '))
        passUsuario = input('Por favor, ingresa la contraseña: ')
        if numeroCuentaUsuario in diccionario_cuentas:
            objeto_Cuenta = diccionario_cuentas[numeroCuentaUsuario]
            saldoActualizado = objeto_Cuenta.deposit(montoDepositoUsuario, passUsuario)
            if saldoActualizado is not None:
                print('Tu nuevo saldo es:', saldoActualizado)
        else:
            print('Número de cuenta no encontrado')

    elif accion == 'o':
        print('*** Abrir Cuenta ***')
        nombreUsuario = input('¿Cuál es el nombre para la nueva cuenta de usuario? ')
        saldoInicialUsuario = int(input('¿Cuál es el saldo inicial para esta cuenta? '))
        passUsuario = input('¿Cuál es la contraseña que deseas utilizar para esta cuenta? ')
        objeto_Cuenta = Cuenta(nombreUsuario, saldoInicialUsuario, passUsuario)
        diccionario_cuentas[nextAccountNumber] = objeto_Cuenta
        print('Tu nuevo número de cuenta es:', nextAccountNumber)
        nextAccountNumber = nextAccountNumber + 1
        print()

    elif accion == 's':
        print('Mostrar:')
        for numeroCuentaUsuario in diccionario_cuentas:
            objeto_Cuenta = diccionario_cuentas[numeroCuentaUsuario]
            print('    Número de cuenta:', numeroCuentaUsuario)
            objeto_Cuenta.show()

    elif accion == 'q':
        break

    elif accion == 'w':
        print('*** Retiro ***')
        numeroCuentaUsuario = int(input('Por favor, ingresa el número de tu cuenta: '))
        montoRetiroUsuario = int(input('Por favor, ingresa la cantidad a retirar: '))
        passUsuario = input('Por favor, ingresa la contraseña: ')
        if numeroCuentaUsuario in diccionario_cuentas:
            objeto_Cuenta = diccionario_cuentas[numeroCuentaUsuario]
            saldoActualizado = objeto_Cuenta.withdraw(montoRetiroUsuario, passUsuario)
            if saldoActualizado is not None:
                print('Retiraste:', montoRetiroUsuario)
                print('Tu nuevo saldo es:', saldoActualizado)
        else:
            print('Número de cuenta no encontrado')

    else:
        print('Lo siento, esa no es una acción válida. Por favor, intenta nuevamente.')

print('Hecho')