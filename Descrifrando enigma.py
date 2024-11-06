def cifrar_mensaje(mensaje, desplazamiento):
    mensaje_cifrado = ''
    for caracter in mensaje:
        if caracter.isalpha(): #si el caracter es letra del alfabeto
            if caracter.isupper(): #si el caracter es mayúscula o minúscula
                #el 97 y 65 son los valores ASCII para las letras mayúsculas y minúsculas
                #el 26 son las letras del alfabeto
                nuevo_caracter = chr((ord(caracter) - 65 + desplazamiento) % 26 + 65)
                #ord sirve para obtener el valor ASCII del caracter
                #se aplica el desplazamiento sumándolo al valor ASCII del caracter
                #se usa aritmética para asegurar que esté el resultado dentro del rango de letras
                #char convierte el valor ASCII resultante de nuevo en un caracter
            else:
                nuevo_caracter = chr((ord(caracter) - 97 + desplazamiento) % 26 + 97)
            mensaje_cifrado += nuevo_caracter
        else:
            mensaje_cifrado += caracter
    return mensaje_cifrado

def descifrar_mensaje(mensaje_cifrado, desplazamiento):
    return cifrar_mensaje(mensaje_cifrado, -desplazamiento)

mensaje = input("Ingrese el mensaje a cifrar o descifrar: ")
desplazamiento = int(input("Ingrese el número de desplazamiento: "))

mensaje_cifrado = cifrar_mensaje(mensaje, desplazamiento)
print("Mensaje cifrado:", mensaje_cifrado)

mensaje_descifrado = descifrar_mensaje(mensaje_cifrado, desplazamiento)
print("Mensaje descifrado:", mensaje_descifrado)
