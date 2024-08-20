# Lista de diccionarios con información de estudiantes
estudiantes = [
    {'nombre': 'Juan', 'edad': 17, 'calificaciones': [85, 90, 88]},
    {'nombre': 'María', 'edad': 19, 'calificaciones': [92, 89, 90]},
    {'nombre': 'Pedro', 'edad': 21, 'calificaciones': [85, 95, 80]},
    {'nombre': 'Ana', 'edad': 18, 'calificaciones': [90, 92, 87]},
    {'nombre': 'Luis', 'edad': 20, 'calificaciones': [88, 85, 92]},
]

# Función para calcular el promedio de una lista de calificaciones
def calcular_promedio(calificaciones):
    return sum(calificaciones) / len(calificaciones)

# Función para determinar si un número es primo
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

# Filtrar y mostrar estudiantes con más de 18 años y promedio de calificaciones superior a 85
print("Estudiantes mayores de 18 años con promedio superior a 85:")
for estudiante in estudiantes:
    if estudiante['edad'] > 18:
        promedio = calcular_promedio(estudiante['calificaciones'])
        if promedio > 85:
            print(f"Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}, Promedio: {promedio:.2f}")

# Calcular el promedio de calificaciones de los estudiantes con más de 18 años y edad primo
promedios_primos = []
for estudiante in estudiantes:
    if estudiante['edad'] > 18 and es_primo(estudiante['edad']):
        promedio = calcular_promedio(estudiante['calificaciones'])
        promedios_primos.append(promedio)

if promedios_primos:
    promedio_general = sum(promedios_primos) / len(promedios_primos)
    print(f"\nPromedio general de calificaciones para estudiantes con edad primo: {promedio_general:.2f}")
else:
    print("\nNo hay estudiantes mayores de 18 años con edad primo.")
