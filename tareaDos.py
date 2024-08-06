

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
def separar_nombres_simple_1(nombres):
    magos_list = []
    cientificos_list = []
    otros_list = []

    for nombre in nombres:
        if nombre in magos:
            magos_list.append(nombre)
        elif nombre in cientificos:
            cientificos_list.append(nombre)
        else:
            otros_list.append(nombre)

    return magos_list, cientificos_list, otros_list


magos_list, cientificos_list, otros_list = separar_nombres_simple_1(nombres)

# Imprimir los resultados
print("\nMagos:", magos_list)
print("\nCientíficos:", cientificos_list)
print("\nOtros:", otros_list)
print("\n")



