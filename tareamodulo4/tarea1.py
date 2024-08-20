# Definición de la clase Animal
class Animal:
    def __init__(self, nombre, raza, edad, peso):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
    
    def comer(self):
        return f"{self.nombre} está comiendo."

    def caminar(self):
        return f"{self.nombre} está caminando."

    def dormir(self):
        return f"{self.nombre} está durmiendo."

    def __str__(self):
        return (f"Nombre: {self.nombre}\n"
                f"Raza: {self.raza}\n"
                f"Edad: {self.edad} años\n"
                f"Peso: {self.peso} kg")

# Definición de la clase Perro que hereda de Animal
class Perro(Animal):
    def __init__(self, nombre, edad, raza, peso):
        super().__init__(nombre, raza, edad, peso)

# Definición de la clase Gato que hereda de Animal
class Gato(Animal):
    def __init__(self, nombre, edad, raza, peso):
        super().__init__(nombre, raza, edad, peso)

# Creación de los objetos Perro y Gato con las características especificadas
perro = Perro(nombre="Brando", edad=3, raza="San Bernardo", peso=30)
gato = Gato(nombre="Roll", edad=4, raza="Persa", peso=3)

# Imprimir información y llamadas a métodos de los objetos
print("Información del Perro:")
print(perro)
print(perro.comer())
print(perro.caminar())
print(perro.dormir())
print()

print("Información del Gato:")
print(gato)
print(gato.comer())
print(gato.caminar())
print(gato.dormir())
