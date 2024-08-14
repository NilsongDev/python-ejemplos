# Crear una lista con 10 números enteros
numeros = [12, 7, 0, -3, 4, 9, 18, 5, 0, -11]

# Recorrer la lista usando la sentencia for
for numero in numeros:
    if numero == 0:
        print(f"El número {numero} es cero.")
    elif numero % 2 == 0:
        print(f"El número {numero} es par.")
    else:
        print(f"El número {numero} es impar.")
