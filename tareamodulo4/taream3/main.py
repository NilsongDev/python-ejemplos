# Definición de la clase Persona
class Persona:
    def __init__(self, nombre, apellidos, sexo, edad, estatura, peso):
        self.nombre = nombre
        self.apellidos = apellidos
        self.sexo = sexo
        self.edad = edad
        self.estatura = estatura
        self.peso = peso

    # Métodos get para acceder a los atributos
    def get_nombre(self):
        return self.nombre

    def get_apellidos(self):
        return self.apellidos

    def get_sexo(self):
        return self.sexo

    def get_edad(self):
        return self.edad

    def get_estatura(self):
        return self.estatura

    def get_peso(self):
        return self.peso

    # Métodos set para modificar los atributos
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_apellidos(self, apellidos):
        self.apellidos = apellidos

    def set_sexo(self, sexo):
        self.sexo = sexo

    def set_edad(self, edad):
        self.edad = edad

    def set_estatura(self, estatura):
        self.estatura = estatura

    def set_peso(self, peso):
        self.peso = peso

    # Método para mostrar la información de la persona
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellidos: {self.apellidos}")
        print(f"Sexo: {self.sexo}")
        print(f"Edad: {self.edad} años")
        print(f"Estatura: {self.estatura} mts")
        print(f"Peso: {self.peso} Kg")

# Creación de los objetos Persona_1 y Persona_2
persona_1 = Persona(nombre="Pedro", apellidos="Vivas", sexo="Masculino", edad=20, estatura=1.78, peso=68)
persona_2 = Persona(nombre="Juan", apellidos="Camargo", sexo="Masculino", edad=18, estatura=1.8, peso=75)

# Modificación de la edad de Persona_1 a 21 años
persona_1.set_edad(21)

# Modificación del apellido de Persona_2 a Santiago
persona_2.set_apellidos("Santiago")

# Mostrar la información actualizada de Persona_1
print("Información actualizada de Persona_1:")
persona_1.mostrar_info()

# Mostrar la información actualizada de Persona_2
print("\nInformación actualizada de Persona_2:")
persona_2.mostrar_info()