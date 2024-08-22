# Solicitar la palabra a buscar y la palabra de reemplazo
palabra_a_buscar = input("Ingresa la palabra a buscar: ")
palabra_de_reemplazo = input("Ingresa la palabra de reemplazo: ")

# Abrir el archivo original en modo de lectura
with open("original.txt", "r") as archivo_original:
    # Leer todo el contenido del archivo
    contenido = archivo_original.read()

# Reemplazar todas las apariciones de la palabra
contenido_modificado = contenido.replace(palabra_a_buscar, palabra_de_reemplazo)

# Guardar el contenido modificado en un nuevo archivo
with open("modificado.txt", "w") as archivo_modificado:
    archivo_modificado.write(contenido_modificado)

print("El archivo ha sido modificado y guardado como 'modificado.txt'.")
