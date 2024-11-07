# Tom ha hecho tiras todos los días y ha registrado sus resultados. Registró los resultados de cada día en una línea,
# de modo que cada línea representa cada día que ha hecho "pull ups".
# Crea un programa que tome el número n y genere el resultado de los días m-th (empezando desde 0)

file=open("/Users/aslea/Documents/Phyton/pull_ups.txt","r")
n=int(input())
cont=file.readlines()[n]
print(cont)

file.close()
