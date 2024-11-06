print("Te encuentras en las afueras de la ciudad. Hay un camino a la izquierda y otro a la derecha.")
eleccion = input("¿Qué camino quieres tomar? (izquierda/derecha): ")

#camino izquierda
if eleccion.lower() == "izquierda": #convertimos todas las letras mayúsculas a minúsculas con .lower
    print("Llegas a una feria pequeña. Hay una carpa de circo adelante.")
    eleccion = input("¿Quieres entrar a ver el show? (si/no): ")

    #si ver show
    if eleccion.lower() == "si":
        print("Entras en la carpa de circo y encuentras unas palomitas con tu nombre.")
        elección = input("¿Quieres comerlas? (si/no): ")
        
        if eleccion.lower() == "si":
            print("Te comes todas las palomitas y al fondo sientes algo y al mirar, te encuentras a la famosa rata con thinner.")
            print("Vomitaste y perdiste el juego")
        else:
            print("De la que te salvaste, bien hecho.")
    
    #no ver show
    else:
        print("Te alejas de la carpa de circo y te encuentras con un peluche de oso.")
        oso = input("¿Quieres llevarlo contigo? (si/no): ")
        print("En la feria te encuentras a un niño perdido.")
        ayuda = input("¿Quieres ayudar al niño a buscar a sus padres? (si/no): ")
        
        if oso.lower() == "si" and ayuda.lower() == "si":
            print("El niño te ha robado tu osito en cuanto te distrajiste. Has perdido el juego y a tu osito.")
        elif ayuda.lower() == "no":
            print("De la que te salvaste, bien hecho.")
        else:
            print("Después de 1 hora buscando, el niño te confesó que nadie podía verlo a él. Te topaste a un niño fantasma, has perdido el juego.")

#camino derecha
elif eleccion.lower() == "derecha": 
    print("Llegas a una cabaña. Hay animales disecados al rededor y un arma en el suelo.")
    eleccion = input("¿Quieres entrar a la cabaña? (si/no): ")

    #si entrar cabaña
    if eleccion.lower() == "si":
        print("Hay un hombre muerto adentro con un costal grande delante.")
        eleccion = input("¿Quieres abrir el costal? (si/no): ")

        if eleccion.lower() == "si":
            print("Al abrir el costal encuentras un montón de alacranes ¡Un alacrán te pica y has perdido el juego!")
        else:
            print("De la que te salvaste, bien hecho.")
    
    #no entrar cabaña
    else:
        print("Te alejas de la cabaña y te encuentras con el elfo Dobby. ¡Dobby te ayuda a encontrar el camino a Hogwarts! Obvio, ganaste el juego")

#opción no válida
else:
    print("Aún no empieza el juego y ya lo perdiste.")