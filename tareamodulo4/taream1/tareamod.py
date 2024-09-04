# personas.py

# Clase base para atributos comunes
class Persona:
    def __init__(self, id, nombre, apellidos, edad):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    def concentrarse(self):
        print(f"{self.nombre} se está concentrando.")

    def viajar(self):
        print(f"{self.nombre} está viajando.")

# Clase para futbolistas
class Futbolista(Persona):
    def __init__(self, id, nombre, apellidos, edad, dolsal, demarcacion):
        super().__init__(id, nombre, apellidos, edad)
        self.dolsal = dolsal
        self.demarcacion = demarcacion

    def jugar_partido(self):
        print(f"{self.nombre} está jugando el partido.")

    def entrenar(self):
        print(f"{self.nombre} está entrenando.")

# Clase para entrenadores
class Entrenador(Persona):
    def __init__(self, id, nombre, apellidos, edad, idfederacion):
        super().__init__(id, nombre, apellidos, edad)
        self.idfederacion = idfederacion

    def dirigir_partido(self):
        print(f"{self.nombre} está dirigiendo el partido.")

    def dirigir_entrenamiento(self):
        print(f"{self.nombre} está dirigiendo el entrenamiento.")

# Clase para masajistas
class Masajista(Persona):
    def __init__(self, id, nombre, apellidos, edad, titulacion, annosexperiencia):
        super().__init__(id, nombre, apellidos, edad)
        self.titulacion = titulacion
        self.annosexperiencia = annosexperiencia

    def dar_masajes(self):
        print(f"{self.nombre} está dando masajes.")
