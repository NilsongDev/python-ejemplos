import random

def adivina_el_numero():
    # Generar un número secreto aleatorio entre 1 y 100
    numero_secreto = random.randint(1, 100)
    
    print("¡Bienvenido al juego de adivinar el número secreto!")
    print("He escogido un número entre 1 y 100. Tienes 5 intentos para adivinarlo.")
    
    # Inicializar el contador de intentos
    intentos = 0
    max_intentos = 5
    
    while intentos < max_intentos:
        # Incrementar el contador de intentos
        intentos += 1
        
        # Pedir al usuario que adivine el número secreto
        try:
            adivinanza = int(input(f"Intento {intentos}/{max_intentos}: Introduce tu adivinanza: "))
        except ValueError:
            print("Por favor, introduce un número válido.")
            continue
        
        # Comparar el número ingresado por el usuario con el número secreto
        if adivinanza > numero_secreto:
            print("El número secreto es menor. Intenta de nuevo.")
        elif adivinanza < numero_secreto:
            print("El número secreto es mayor. Intenta de nuevo.")
        else:
            print("¡Felicidades! Has adivinado el número secreto.")
            break
    else:
        # Si se alcanzó el número máximo de intentos sin adivinar
        print(f"Lo siento, has agotado tus {max_intentos} intentos. El número secreto era {numero_secreto}.")

# Llamar a la función para iniciar el juego
adivina_el_numero()