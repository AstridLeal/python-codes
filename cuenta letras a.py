import time

texto = "Amanda, Ana y Andrea van a la playa a tomar el sol y comer papaya. Caminan por la arena y ven aves volar sobre el agua. Ana agarra una guitarra y canta una canción mientras Amanda toma una foto de la escena. Andrea se acuesta en la toalla y lee una novela. Disfrutan de un día maravilloso en la costa."

contador_a = 0

start_time = time.time()

for letra in texto:
    if letra == 'a' or letra == 'A':
        contador_a += 1

end_time = time.time()
#comentario
print("El número total de letras 'a' es:", contador_a)
print("El programa tardó {:.15f} segundos en ejecutarse".format(end_time - start_time))
