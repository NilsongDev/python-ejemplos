#asdasd
# #Objetivo: Crear un programa que permita al usuario adivinar un número secreto. 
# El programa debe dar una sola oportunidad al usuario para adivinar 
# y debe indicar si el usuario adivinó correctamente o no.

# Instrucciones:

# Genera un número secreto.
# Pide al usuario que adivine el número.
# Usa estructuras if y else para comparar 
# la adivinanza del usuario con el número secreto.
# Indica al usuario si su adivinanza es correcta o no.


import random

# Generar un número secreto entre 1 y 10
numero_secreto = random.randint(1, 10)

# Pedir al usuario que adivine el número
adivinanza = int(input("Adivina el número secreto (entre 1 y 10): "))

# Comparar la adivinanza del usuario con el número secreto
if adivinanza == numero_secreto:
    print("¡Felicidades! Adivinaste el número secreto.")
else:
    print(f"Lo siento, no adivinaste. El número secreto era {numero_secreto}.")


