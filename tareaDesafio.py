# Función para calcular el precio final con descuento
def calcular_precio_final(precio_inicial, descuento):
    # Verificar que el descuento esté en el rango válido (0 a 100)
    if descuento < 0 or descuento > 100:
        return "Descuento inválido"
    
    # Calcular el precio final aplicando el descuento
    precio_final = precio_inicial * (1 - descuento / 100)
    
    # Retornar el precio final calculado
    return precio_final

# Solicitar el precio inicial al usuario
precio_inicial = float(input("Ingresa el precio inicial del producto: "))

# Solicitar el descuento al usuario
descuento = float(input("Ingresa el porcentaje de descuento: "))

# Llamar a la función para calcular el precio final
resultado = calcular_precio_final(precio_inicial, descuento)

# Mostrar el resultado
print("El precio final del producto es:", round( resultado))
