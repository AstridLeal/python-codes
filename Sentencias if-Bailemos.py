# Se te ha pedido que coordines el concurso de la escuela de baile.
# Las condiciones del concurso son las siguientes:
# -Si la puntuación es 80 o más, el participante recibe un certificado
# -Si la puntuación es 90 o más, el participante obtiene un certificado y también es admitido a la escuela.
# El programa dado toma la puntuación como entrada.

calif=int(input())
if calif>=80:
    print("certificate")
    if calif>=90:
        print("admitted")