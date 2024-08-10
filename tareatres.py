
#variables asignadas
a=20
b=30





#funcion que acepta dos valores
def funcion_multiplicar (varlo1,valor2):
    print("holaaaaa")
    #la variable total guarda el resultado del ejercicio de multiplicacion
    total = varlo1 * valor2

    #un print para mostrar el resultado
    print(f"el total de la multiplicacion es : {total}")

#se llama a la funcion y se le asigna las variables para que se ejecute
funcion_multiplicar(a,b)









#la otra manera que se puede hacer es con lambda en mas corto de lo normal

multiplicacion = lambda a,b :  a * b
print("este es el valor por lambda : ",multiplicacion(a,b))