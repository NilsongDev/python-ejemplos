# Abrir el archivo en modo de lectura
with open("tareas.txt", "r") as archivo:
    # Leer todo el contenido del archivo
    contenido = archivo.read()

# Dividir el contenido en palabras
palabras = contenido.split()

# Contar el número de palabras
numero_de_palabras = len(palabras)

# Mostrar el resultado en la consola
print(f"El archivo contiene {numero_de_palabras} palabras.")
