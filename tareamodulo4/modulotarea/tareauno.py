# Abrir el archivo original en modo de lectura
with open("original.txt", "r") as archivo_original:
    # Leer todo el contenido del archivo original
    contenido = archivo_original.read()

# Abrir el archivo de destino en modo de escritura
with open("copia.txt", "w") as archivo_copia:
    # Escribir el contenido en el nuevo archivo
    archivo_copia.write(contenido)

print("El contenido se ha copiado exitosamente a 'copia.txt'.")
