# Programa convertidor de Celsius a Fahrenheit
# Ecuacion para Farenheit: 9/5 * celsius + 32

celsius=float(int(input()))

def conv(x):
    f=(9.0/5.0)*celsius+32
    print(f)

conv(celsius)