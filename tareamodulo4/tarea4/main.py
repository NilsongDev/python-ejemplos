#   clase Libro 
class Libro:
    pass  # La clase Libro está definida 

#  dos instancias 
libro_1 = Libro()
libro_2 = Libro()

#  Asignar atributos 
libro_1.autor = 'Dan Brown'
libro_1.titulo = 'Infierno'

libro_2.autor = 'Dan Brown'
libro_2.titulo = 'El Código Da Vinci'
libro_2.ann_de_publicacion = 2003

#   Imprimir el valor 
print(libro_1.__dict__)
print(libro_2.__dict__)
