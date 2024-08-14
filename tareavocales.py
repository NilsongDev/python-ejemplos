# Palabra original
palabra = "paralelepípedo"

# Definir las vocales
vocales = "aeiouáéíóú"

# Recorrer la palabra y eliminar las vocales, imprimiendo las consonantes y sus posiciones
for i, letra in enumerate(palabra):
    if letra.lower() not in vocales:
        print(f"Consonante: {letra}, Posición: {i}")