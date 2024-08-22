# Abrir (o crear) el archivo en modo de escritura
with open("tareas.txt", "w") as archivo:
    while True:
        # Pedir al usuario que ingrese una tarea
        tarea = input("Ingresa una tarea (escribe 'salir' para terminar): ")
        
        # Si el usuario escribe 'salir', terminamos el bucle
        if tarea.lower() == "salir":
            break
        
        # Escribir la tarea en el archivo, seguida de un salto de línea
        archivo.write(tarea + "\n")

print("Las tareas se han guardado en 'tareas.txt'.")