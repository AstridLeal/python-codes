# 3 tipos de datos que no sean string o lista
entero = 15
decimal = 14.6
booleano = True  

# Imprimimos el tipo de cada variable
print(type(entero))  
print(type(decimal))  
print(type(booleano)) 

# Verificamos si todas las variables son clases de type:
son_clases = all(isinstance(variable, type) for variable in [entero, decimal, booleano]) 
print("¿Todas las variables son clases?", son_clases) 

# Se usa isinstance() para verificar si cada variable es una instancia de la clase type
# Cada ariable se compara con la clase type, que es la clase base de todos los tipos de datos y no distingue entre tipos primitivos y clases

# Verificamos si todas las variables son clases específicas que representan el tipo de dato esperado:
son_clases_especificas = all(isinstance(variable, clase_especifica) for variable, clase_especifica in zip([entero, decimal, booleano], [int, float, bool]))
print("¿Todas las variables son instancias de sus clases específicas?", son_clases_especificas) 

# Se usa zip() para crear pares de elementos (variable, clase)
