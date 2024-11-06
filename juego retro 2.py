nombre = input("Ingresa tu nombre: ")
print(f"Hola {nombre}, bienvenido a mi juego retro.")

print(f"Te encuentras en las afueras de la ciudad, {nombre}. Hay un camino a la izquierda y otro a la derecha.")
eleccion = input("¿Qué camino quieres tomar? (izquierda/derecha): ")

#camino izquierda
if eleccion.lower() == "izquierda": #convertimos todas las letras mayúsculas a minúsculas con .lower
    print(f"Llegas a una feria pequeña. Hay una carpa de circo adelante de ti, {nombre}.")
    eleccion = input("¿Quieres entrar a ver el show? (si/no): ")

    #si ver show
    if eleccion.lower() == "si":
        print("Entras en la carpa de circo y encuentras unas palomitas con tu nombre.")
        elección = input("¿Quieres comerlas? (si/no): ")
        
        if eleccion.lower() == "si":
            print("Te comes todas las palomitas y al fondo sientes algo y al mirar, te encuentras a la famosa rata con thinner.")
            print(f"Vomitaste y perdiste el juego {nombre}.")
        else:
            print(f"De la que te salvaste, bien hecho {nombre}.")
    
    #no ver show
    else:
        print("Te alejas de la carpa de circo y te encuentras con un peluche de oso.")
        oso = input(f"¿Quieres llevarlo contigo, {nombre}? (si/no): ")
        print("En la feria te encuentras a un niño perdido.")
        ayuda = input("¿Quieres ayudar al niño a buscar a sus padres? (si/no): ")
        
        if oso.lower() == "si" and ayuda.lower() == "si":
            print(f"El niño te ha robado tu osito en cuanto te distrajiste. Has perdido el juego y a tu osito, {nombre}.")
        elif ayuda.lower() == "no":
            print(f"De la que te salvaste, bien hecho {nombre}.")
        else:
            print("Después de 1 hora buscando, el niño te confesó que nadie podía verlo a él. Te topaste a un niño fantasma, has perdido el juego.")

#camino derecha
elif eleccion.lower() == "derecha": 
    print("Llegas a una cabaña. Hay animales disecados al rededor y un arma en el suelo.")
    eleccion = input("¿Quieres entrar a la cabaña? (si/no): ")

    #si entrar cabaña
    if eleccion.lower() == "si":
        print("Hay un hombre muerto adentro, con un costal grande delante.")
        eleccion = input("¿Quieres abrir el costal? (si/no): ")

        if eleccion.lower() == "si":
            print(f"Al abrir el costal encuentras un montón de alacranes ¡Un alacrán te pica y has perdido el juego {nombre}!")
        else:
            print(f"De la que te salvaste, bien hecho {nombre}.")  
            eleccion = input(f"Continuas paseando por la cabaña y te encuentras con una serpiente. ¿Qué quieres hacerle {nombre}? (hablar/atacar/correr): ")
            if eleccion.lower() == "hablar":
                print(f"Has hablado en pársel con la serpiente y te ha regalado la posión de 'Siempre felices'. Has ganado el juego {nombre}.")
            if eleccion.lower() == "correr":
                print(f"Saliste corriendo de la cabaña y atropellaste a un bebé oso. Mamá oso te ha hecho perder el juego {nombre}.")
            if eleccion.lower() == "atacar":
                print(f"La serpiente ha sido más rápida que tú y te ha sacado los ojos. Ah, también te sacó del juego {nombre}.")
    
    #no entrar cabaña
    else:
        print("Te alejas de la cabaña y te encuentras con el elfo Dobby. ¡Dobby te ayuda a encontrar el camino a Hogwarts!")
        eleccion = input(f"Dobby quiere saber a qué casa pertenece {nombre}. (‎Gryffindor/Hufflepuff/Ravenclaw/Slytherin): ")
        if "g" in eleccion.lower(): 
            print(f"Excelente casa, {nombre}.")
        elif "p" in eleccion.lower() or "w" in eleccion.lower(): 
            print(f"Nada mal, {nombre}.")
        else:
            print(f"Mientras no seas un sangre sucia, {nombre}, tendrás oportunidad.")
        
#opción no válida
else:
    print(f"Aún no empieza el juego y ya lo perdiste {nombre}.")
