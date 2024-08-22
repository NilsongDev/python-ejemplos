# Abrir el archivo en modo de lectura
with open("archivo.txt", "r") as archivo:
    # Leer todas las líneas del archivo
    lineas = archivo.readlines()

# Contar el número de líneas
numero_de_lineas = len(lineas)

# Mostrar el resultado en la consola
print(f"El archivo tiene {numero_de_lineas} líneas.")
