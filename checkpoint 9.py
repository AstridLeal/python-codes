def explorar_territorio(herramienta1, herramienta2):
    #CONDICION 1 LONGITUD DE LA PALABRA
  if len(herramienta1) > len(herramienta2):
    resultado = f"¡La herramienta '{herramienta1}' ganó por su longitud."
  elif len(herramienta2) > len(herramienta1):
    resultado = f"La herramienta '{herramienta2}' ganó por su longitud."
    #CONDICION 2 CANTIDAD DE VOCALES
  elif herramienta1.count("a") + herramienta1.count("e") + herramienta1.count("i") + herramienta1.count("o") + herramienta1.count("u") > herramienta2.count("a") + herramienta2.count("e") + herramienta2.count("i") + herramienta2.count("o") + herramienta2.count("u"):
    resultado = f"¡La herramienta '{herramienta1}' ganó por tener más vocales."
  elif herramienta2.count("a") + herramienta2.count("e") + herramienta2.count("i") + herramienta2.count("o") + herramienta2.count("u") > herramienta1.count("a") + herramienta1.count("e") + herramienta1.count("i") + herramienta1.count("o") + herramienta1.count("u"):
    resultado = f"La herramienta '{herramienta2}' ganó por tener más vocales."
  else:
    resultado = "Usa otras herramientas."
  return resultado

herramienta1 = input("Herramienta 1: ")
herramienta2 = input("Herramienta 2: ")

print(explorar_territorio(herramienta1, herramienta2))