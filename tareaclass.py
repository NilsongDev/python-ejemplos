



class Book:
    def __init__(self, title, fecha):
        self.title = title
        self.fecha = fecha

# Crear instancias de la clase Book con título y fecha
Book1 = Book("hola", "2024-08-11")
Book2 = Book("chao", "2024-08-10")

# Imprimir el título y la fecha de los libros
print(f"Titulo: {Book1.title}, Fecha: {Book1.fecha}")
print(f"Titulo: {Book2.title}, Fecha: {Book2.fecha}")