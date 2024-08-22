# Lista original
mi_lista = [5, 20, 15, 20, 25, 50, 20, 5, 18, 15]

# 1. Eliminar los elementos duplicados usando un set y luego convertirlo de nuevo a lista
mi_lista_sin_duplicados = list(set(mi_lista))

# 2. Ordenar la lista resultante en orden ascendente
mi_lista_sin_duplicados.sort()

# Imprimir la lista final
print(mi_lista_sin_duplicados)
