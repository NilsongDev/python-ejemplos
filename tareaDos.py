

# Lista inicial de nombres
nombres = [
    "Harry Houdini",
    "Newton",
    "David Blaine",
    "Hawking",
    "Messi",
    "Teller",
    "Einstein",
    "Pele",
    "Juandes"
]

# Listas de magos y científicos
magos = ["Harry Houdini", "David Blaine", "Teller"]
cientificos = ["Newton", "Hawking", "Einstein"]

# Función para separar los nombres en tres grupos
def separar_nombres(nombres):
    global magos, cientificos
    magos_list = [nombre for nombre in nombres if nombre in magos]
    cientificos_list = [nombre for nombre in nombres if nombre in cientificos]
    otros_list = [nombre for nombre in nombres if nombre not in magos and nombre not in cientificos]
    return magos_list, cientificos_list, otros_list

# Función para modificar la lista de magos
def hacer_grandioso():
    global magos
    magos = [f"El gran {mago}" for mago in magos]

# Función para imprimir los nombres de la lista
def imprimir_nombres():
    global nombres
    for nombre in nombres:
        print(nombre)

# Separar los nombres en grupos
magos_list, cientificos_list, otros_list = separar_nombres(nombres)

# Imprimir la lista completa antes de la modificación
print("Lista completa antes de la modificación:")
imprimir_nombres()

# Modificar los nombres de los magos
hacer_grandioso()

# Imprimir los nombres de los magos grandiosos
print("\nMagos grandiosos:")
imprimir_nombres()

# Imprimir los nombres de los científicos
print("\nCientíficos:")
for cientifico in cientificos_list:
    print(cientifico)

# Imprimir los nombres restantes
print("\nOtros:")
for otro in otros_list:
    print(otro)