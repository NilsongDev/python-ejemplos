def obtener_informacion_contacto():
    # Obtener información desde la consola
    nombre = input("Ingresa el nombre del contacto: ")
    print("\n")
    correo = input("Ingresa el correo electrónico del contacto: ")
    print("\n")
    telefono = input("Ingresa el número de teléfono del contacto: ")
    print("\n")
    
    # Almacenar la información en un diccionario
    contacto = {
        "Nombre": nombre,
        "Correo": correo,
        "Teléfono": telefono
    }
    
    return contacto

def operaciones_basicas(contacto):
    # Calcular el número total de caracteres en el nombre del contacto
    caracteres_nombre = len(contacto["Nombre"])
    
    # Imprimir la información completa del contacto
    print("\nInformación del contacto:")
    print("+--------------------------------------------+")
    print("|       Campo       |          Valor         |")
    print("+--------------------------------------------+")
    print(f"| Nombre            | {contacto['Nombre']}")
    print(f"| Correo            | {contacto['Correo']}")
    print(f"| Teléfono          | {contacto['Teléfono']}")
    print(f"| Caracteres Nombre | {caracteres_nombre}")
    print("+--------------------------------------------+")

def main():
    contacto = obtener_informacion_contacto()
    operaciones_basicas(contacto)

if __name__ == "__main__":
    main()


