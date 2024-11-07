#Realizado por Astrid A. Leal Carrillo
import random
#Aquí defino a mis elementos clave
#Los 'individuos' serían mis clases y los 'cromosomas' las sesiones
individuos = 7
cromosomas = 6
generaciones = 6 #Mi Crossover

#Creo el arreglo con mis clases y sesiones
poblacion = [[0 for x in range(cromosomas)] for x in range(individuos)]

print("POBLACION INICIAL")

#Lleno la población aleatoriamente
for individuo in range(individuos):
    for cromosoma in range(cromosomas):
        poblacion[individuo][cromosoma] = random.randint(0, 1)

#Función para sacar el fitness
def medir_aptitud(poblacion):
    aptitud = [0 for i in range(individuos)]
    valores = ["+/-",2 ** 3, 2 ** 2, 2 ** 1, 2 ** 0, 2 ** -1, 2 ** -2]
    print("\nVALORES PARA DETERMINAR EL FITNESS IDEAL")
    print(valores)

#Multiplico la lista fitness por cada clase de la población
    for individuo in range(individuos):
        for cromosoma in range(1, cromosomas):
            aptitud[individuo] += poblacion[individuo][cromosoma] * valores[cromosoma]
        #Cambio signo según el valor
        if poblacion[individuo][0] == 1:
            aptitud[individuo] *= -1

    #Imprimo los valores del fitness de cada clase o sesión
    print("\nFITNESS")
    for individuo in range(individuos):
        print(str(individuo) + " - [" + ", ".join(str(f) for f in poblacion[individuo]) + "] = " + "{:.9}".format(aptitud[individuo])) #Aquí me aseguro de que al imprimir la lista no saldrán los corchetes ni las comas

#Imprimo el fitness total de la poblacion
    total_aptitud = 0
    for x in range(individuos):
        total_aptitud += abs(aptitud[x])
    print("TOTAL FITNESS " + str(total_aptitud))
    print("")
    return aptitud


#Función para apostar entre cada par de clases (gana la que tenga mayor fitness)
def torneo(indice_individuo1, indice_individuo2):
    print("TORNEO")
    print(str(indice_individuo1) + " - [" + ", ".join(str(f) for f in poblacion[indice_individuo1]) + "] = " + "{:.9}".format(aptitud[indice_individuo1]))
    print(str(indice_individuo2) + " - [" + ", ".join(str(f) for f in poblacion[indice_individuo2]) + "] = " + "{:.9}".format(aptitud[indice_individuo2]))
    if abs(aptitud[indice_individuo1]) > abs(aptitud[indice_individuo2]):
        indice_ganador = indice_individuo1
    else:
        indice_ganador = indice_individuo2
    print("GANADOR")
    print(str(indice_ganador) + " - [" + ", ".join(str(f) for f in poblacion[indice_ganador]) + "] = " + "{:.9}".format(aptitud[indice_ganador]))
    print("")
    return indice_ganador

#Función para aplicar la mutación de forma aleatoria a cada individuo (clase). Va a cambiar de 1 a 0 un bit elegido al azar
def mutacion(indice_individuo):
    print("MUTACIÓN")
    print(str(indice_individuo) + " - [" + ", ".join(str(f) for f in poblacion[indice_individuo]) + "]")
    indice_mutado = random.randint(0, cromosomas - 1)
    if poblacion[indice_individuo][indice_mutado] == 0:
        poblacion[indice_individuo][indice_mutado] = 1
    else:
        poblacion[indice_individuo][indice_mutado] = 0
    print(str(indice_individuo) + " - [" + ", ".join(str(f) for f in poblacion[indice_individuo]) + "]")
    print("")

#Función de cruce que decodifica los valores de los hijos correspondientes a la nueva poblacón. La posición del bit se elige al azar
def cruce(indice_individuo1, indice_individuo2):
    print("CRUCE")
    print(str(indice_individuo1) + " - [" + ", ".join(str(f) for f in poblacion[indice_individuo1]) + "]")
    print(str(indice_individuo2) + " - [" + ", ".join(str(f) for f in poblacion[indice_individuo2]) + "]")
    indice_cruce = random.randint(1, cromosomas - 1)
    print("Índice de cruce " + str(indice_cruce));
    print("Descendencias")
    descendencia1 = poblacion[indice_individuo1][:indice_cruce] + poblacion[indice_individuo2][indice_cruce:]
    print(descendencia1)
    descendencia2 = poblacion[indice_individuo2][:indice_cruce] + poblacion[indice_individuo1][indice_cruce:]
    print(descendencia2)
    return descendencia1, descendencia2

#Imprimo la población
def imprime_poblacion():
    for individuo in range(individuos):
        print(str(individuo) + " - [" + ", ".join(str(f) for f in poblacion[individuo]) + "]")

for generacion in range(generaciones):
    print("\n--------- GENERACIÓN " + str(generacion) +" ---------")
    imprime_poblacion()
    nueva_generacion = [0 for x in range(individuos)]
    aptitud = medir_aptitud(poblacion)
    for i in range(individuos // 2):
        individuo_ganador = torneo(i, individuos - 1 -i)
        nueva_generacion[i] = poblacion[individuo_ganador]
    mutaciones = random.randint(0, individuos // 2)
    for j in range(mutaciones):
        mutacion(random.randint(0, mutaciones))
    indice_hijos = individuos // 2
    for k in range(0, individuos // 2, 2):
        nueva_generacion[indice_hijos], nueva_generacion[indice_hijos + 1] = cruce(k, k+1)
        indice_hijos += 2
        print("")
    poblacion = nueva_generacion
print("\n------- ÚLTIMA GENERACIÓN -------")
imprime_poblacion()
medir_aptitud(poblacion)

#Aqui imprimo las clases
i=0
while i<=10:
    file=open("/Users/aslea/Documents/Phyton/Tarea/datos.txt",encoding="utf8")
    x=random.randint(1, 60)
    cont=file.readlines()[x]
    print(cont)
    file.close()
    i+=1