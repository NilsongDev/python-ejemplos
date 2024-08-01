def obtener_datos_personales():
    personas = []
    for i in range(1, 4):
        print(f"Persona {i}:")
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        altura = float(input("Altura (en metros): "))
        personas.append((nombre, edad, altura))
    return personas

def calcular_promedios_y_totales(personas):
    total_edades = sum(persona[1] for persona in personas)
    total_alturas = sum(persona[2] for persona in personas)
    total_caracteres_nombres = sum(len(persona[0]) for persona in personas)
    
    promedio_edades = total_edades / len(personas)
    promedio_alturas = total_alturas / len(personas)
    
    return promedio_edades, promedio_alturas, total_caracteres_nombres

def mostrar_resultados(promedio_edades, promedio_alturas, total_caracteres_nombres):
    print(f"\nPromedio de edades: {promedio_edades:.2f}")
    print(f"Promedio de alturas: {promedio_alturas:.2f} metros")
    print(f"Total de caracteres en los nombres: {total_caracteres_nombres}")

def main():
    personas = obtener_datos_personales()
    promedio_edades, promedio_alturas, total_caracteres_nombres = calcular_promedios_y_totales(personas)
    mostrar_resultados(promedio_edades, promedio_alturas, total_caracteres_nombres)

if __name__ == "__main__":
    main()