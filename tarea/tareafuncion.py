def calcular_area_rectangulo(base, altura):
    # Validar que ambos parámetros sean números positivos
    if base <= 0 or altura <= 0:
        return "Error: La base y la altura deben ser números positivos."
    
    # Calcular el área del rectángulo
    area = base * altura
    
    return area

# Ejemplo de uso de la función
base = 5
altura = 10
resultado = calcular_area_rectangulo(base, altura)

print(f"El área del rectángulo es: {resultado}")
