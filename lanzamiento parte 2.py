tareas = ["Revisar el sistema de propulsión", "Verificar el sistema de navegación", "Comprobar los niveles de combustible", "Asegurarse de que todos los sistemas estén en verde", "Verificar Nivel de Oxígeno"]

print("Lista de verificación de último minuto para el lanzamiento al espacio:")
for i, tarea in enumerate(tareas, 1):
    print(f"{i}. {tarea}")

for tarea in tareas:
  tarea_completada = False
  while not tarea_completada:
    respuesta = input(f"¿{tarea} completada? (s/n): ").lower()
    if respuesta == "s":
      tarea_completada = True
    else:
      print("La tarea debe ser completada antes de continuar.")

print("\n¡Preparativos completados! ¡Todo listo para el lanzamiento al espacio!")
