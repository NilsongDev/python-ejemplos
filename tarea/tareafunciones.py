# Función para sumar dos números
def sumar(num1, num2):
    return num1 + num2

# Función para restar dos números
def restar(num1, num2):
    return num1 - num2

# Función para multiplicar dos números
def multiplicar(num1, num2):
    return num1 * num2

# Función para dividir dos números
def dividir(num1, num2):
    # Validar que el divisor no sea cero
    if num2 == 0:
        return "Error: No se puede dividir entre cero."
    return num1 / num2

# Función que acepta dos números y regresa una tupla con los resultados de suma, resta, multiplicación y división
def operaciones(num1, num2):
    suma = sumar(num1, num2)
    resta = restar(num1, num2)
    multiplicacion = multiplicar(num1, num2)
    division = dividir(num1, num2)
    
    return (suma, resta, multiplicacion, division)

# Función para crear un diccionario con los resultados de las operaciones
def resultados_en_diccionario(num1, num2):
    resultados = operaciones(num1, num2)
    diccionario = {
        'Suma': resultados[0],
        'Resta': resultados[1],
        'Multiplicación': resultados[2],
        'División': resultados[3]
    }
    return diccionario

# Ejemplo de uso de las funciones
num1 = 10
num2 = 5
diccionario_resultados = resultados_en_diccionario(num1, num2)

print("Resultados:")
for clave, valor in diccionario_resultados.items():
    print(f"{clave}: {valor}")
