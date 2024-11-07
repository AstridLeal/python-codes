# Programa que permite a los usuarios crear sus propios códigos PIN para sus tarjetas bancarias.
# Cada código PIN consiste en dígitos. 


try:
    pin=int(input())
    print("PIN code is created")

except ValueError:
    print("Please enter a number")