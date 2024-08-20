# Clase base
class Figura:
    def __init__(self, lado):
        self._lado = lado
    
    @property
    def lado(self):
        return self._lado
    
    @lado.setter
    def lado(self, valor):
        if valor <= 0:
            raise ValueError("El lado debe ser un número positivo.")
        self._lado = valor
    
    def calcular_perimetro(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases.")

# Clase Cuadrado
class Cuadrado(Figura):
    def calcular_perimetro(self):
        return self.lado * 4

# Clase Pentagono
class Pentagono(Figura):
    def calcular_perimetro(self):
        return self.lado * 5

# Clase Exagono
class Exagono(Figura):
    def calcular_perimetro(self):
        return self.lado * 6

# Clase Octagono
class Octagono(Figura):
    def calcular_perimetro(self):
        return self.lado * 8

# Crear instancias de cada figura
octagono = Octagono(5)
pentagono = Pentagono(5)
cuadrado = Cuadrado(5)
exagono = Exagono(5)


# Imprimir perímetros
print(f"Perímetro del octágono: {octagono.calcular_perimetro()}")
print(f"Perímetro del pentágono: {pentagono.calcular_perimetro()}")
print(f"Perímetro del cuadrado: {cuadrado.calcular_perimetro()}")
print(f"Perímetro del exágono: {exagono.calcular_perimetro()}")

