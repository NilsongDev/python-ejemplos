# Solicitar al usuario que ingrese tres números diferentes
numero1 = round( float(input("Ingresa el primer número: ")))
numero2 = round( float(input("Ingresa el segundo número: ")))
numero3 = round( float(input("Ingresa el tercer número: ")))

# Ordenar los números de mayor a menor
if numero1 > numero2:
    if numero1 > numero3:
        if numero2 > numero3:
            print(f"El orden es: {numero1}, {numero2}, {numero3}")
        else:
            print(f"El orden es: {numero1}, {numero3}, {numero2}")
    else:
        print(f"El orden es: {numero3}, {numero1}, {numero2}")
else:
    if numero2 > numero3:
        if numero1 > numero3:
            print(f"El orden es: {numero2}, {numero1}, {numero3}")
        else:
            print(f"El orden es: {numero2}, {numero3}, {numero1}")
    else:
        print(f"El orden es: {numero3}, {numero2}, {numero1}")
