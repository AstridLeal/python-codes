#checkpoint 6

entrada = bool(input("¿Tiene entrada o pulsera? (True/False): "))
adulto = bool(input("¿Es usted adulto? (True/False): "))
alcohol_drogas = bool(input("¿Está bajo efectos de alcohol o drogas? (True/False): "))

if entrada and adulto and not alcohol_drogas:
    print("¡Acceso permitido!")
else:
    print("Acceso denegado.")

if not entrada:
    print("No tiene entrada o pulsera.")
if not adulto:
    print("Debe ser adulto para acceder.")
if alcohol_drogas:
    print("No se permite el acceso bajo la influencia de alcohol o drogas.")