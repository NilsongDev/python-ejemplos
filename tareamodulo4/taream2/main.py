# Definición de la clase Animal
class Animal:
    def __init__(self, nombre, raza, edad, peso):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Raza: {self.raza}")
        print(f"Edad: {self.edad} años")
        print(f"Peso: {self.peso} kg")

# Creación de la instancia para el caballo
caballo = Animal(nombre="Zeus", raza="Pura sangre", edad=5, peso=450)

# Creación de la instancia para el león
leon = Animal(nombre="Boulder", raza="Atlas", edad=10, peso=130)

# Mostrar la información del caballo
print("Información del Caballo:")
caballo.mostrar_info()

# Mostrar la información del león
print("\nInformación del León:")
leon.mostrar_info()