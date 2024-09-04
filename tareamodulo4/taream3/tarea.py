# Definición de la clase Persona
class Persona:
    def __init__(self, id, nombre, apellido):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido

    def obtener_datos(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Apellido: {self.apellido}"

# Definición de la clase Estudiante que hereda de Persona
class Estudiante(Persona):
    def __init__(self, id, nombre, apellido, codigo, matricula):
        super().__init__(id, nombre, apellido)
        self.codigo = codigo
        self.matricula = matricula

    def obtener_datos(self):
        datos_persona = super().obtener_datos()
        return f"{datos_persona}, Código: {self.codigo}, Matrícula: {self.matricula}"

# Creación de instancias y muestra de datos
persona = Persona(id=123456, nombre="Juan", apellido="Pérez")
estudiante = Estudiante(id=789012, nombre="Ana", apellido="Gómez", codigo="A1234", matricula="M5678")

print("Datos de la Persona:")
print(persona.obtener_datos())

print("\nDatos del Estudiante:")
print(estudiante.obtener_datos())