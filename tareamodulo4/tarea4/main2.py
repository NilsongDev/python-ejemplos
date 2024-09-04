# Clase persona
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def movimiento(self):
        return f"{self.nombre} está caminando"

# Subclase Maratonista 
class Maratonista(Persona):
    def movimiento(self):
        return f"{self.nombre} está trotando"

# subclase ciclista 
class Ciclista(Persona):
    def movimiento(self):
        return f"{self.nombre} está rodando"

# ejemplo de uso
persona = Persona("Juan")
maratonista = Maratonista("Ana")
ciclista = Ciclista("Luis")

print(persona.movimiento())       # Salida: Juan está caminando
print(maratonista.movimiento())   # Salida: Ana está trotando
print(ciclista.movimiento())      # Salida: Luis está rodando
