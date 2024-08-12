"""

Requerimos crear un registro de datos personales de tres personas. Los datos que se necesitan
son: su nombre, apellido y teléfono. Para ello, generaremos un diccionario para cada una de las
personas con los datos mencionados, y luego los almacenaremos dentro de una lista. Finalmente,
imprimiremos en pantalla la lista.






"""
# Lista para almacenar los diccionarios de las personas
lista_personas = []

# Solicitar datos de tres personas
for i in range(3):
    print(f"Ingresando datos para la persona {i + 1}:")
    
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    telefono = input("Teléfono: ")
    
    # Crear un diccionario para cada persona
    persona = {
        "nombre": nombre,
        "apellido": apellido,
        "teléfono": telefono
    }
    
    # Añadir el diccionario a la lista
    lista_personas.append(persona)

# Imprimir la lista de personas
print("\nLista de personas ingresadas:")
for persona in lista_personas:
    print(f"Nombre: {persona['nombre']}, Apellido: {persona['apellido']}, Teléfono: {persona['teléfono']}")






































