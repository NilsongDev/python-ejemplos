# main.py

from tareamod import Futbolista, Entrenador, Masajista

def main():
    # codigo para las  instancias de las clases
    futbolista = Futbolista(id=1, nombre="Juan", apellidos="Pérez", edad=25, dolsal=10, demarcacion="Delantero")
    entrenador = Entrenador(id=2, nombre="Carlos", apellidos="Gómez", edad=45, idfederacion="FIFA123")
    masajista = Masajista(id=3, nombre="Luis", apellidos="Martínez", edad=38, titulacion="Diplomado en Fisioterapia", annosexperiencia=15)

    # se llaman a los metodos de los futbolistas
    futbolista.concentrarse()
    futbolista.viajar()
    futbolista.jugar_partido()
    futbolista.entrenar()

    print()  # separar tipo br
# se llaman a los metodos de los entrenador
    entrenador.concentrarse()
    entrenador.viajar()
    entrenador.dirigir_partido()
    entrenador.dirigir_entrenamiento()

    print()  
# se llaman a los metodos de los masajista
    masajista.concentrarse()
    masajista.viajar()
    masajista.dar_masajes()

if __name__ == "__main__":
    main()