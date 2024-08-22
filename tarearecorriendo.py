# Lista de listas original
listas = [[1, 2, 3], [0, 4, 5], [4, 0, 1], [6, 5, 4]]

# Diccionario para asignar sublistas a claves
diccionario = {}

# Recorrer las listas con índices
for i, sublista in enumerate(listas):
    # Si el primer número de la sublista es cero, omitir toda la sublista
    if sublista[0] == 0:
        continue
    
    # Filtrar ceros en la sublista y preparar la sublista para imprimir
    sublista_filtrada = [num for num in sublista if num != 0]
    
    # Imprimir la sublista filtrada
    print(f"{chr(65 + i)}: {sublista_filtrada}")
    
    # Asignar la sublista filtrada al diccionario con la clave correspondiente
    clave = chr(65 + i)  # 65 es el código ASCII de 'A'
    diccionario[clave] = sublista_filtrada

# Imprimir el diccionario resultante
print("\nDiccionario resultante:")
print(diccionario)
