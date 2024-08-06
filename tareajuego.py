import random

def jugar():
    opciones = ["piedra", "papel", "tijera"]
    puntaje_jugador = 0
    puntaje_computadora = 0

    while True:
        print("\nOpciones: piedra, papel, tijera")
        eleccion_jugador = input("Elige tu opción (o escribe 'salir' para terminar): ").lower()
        
        if eleccion_jugador == 'salir':
            print(f"\nGracias por jugar. Puntaje final - Jugador: {puntaje_jugador}, Computadora: {puntaje_computadora}")
            break
        
        if eleccion_jugador not in opciones:
            print("Opción inválida, por favor elige piedra, papel o tijera.")
            continue
        
        eleccion_computadora = random.choice(opciones)
        print(f"La computadora eligió: {eleccion_computadora}")

        if eleccion_jugador == eleccion_computadora:
            print("¡Es un empate!")
        elif (eleccion_jugador == "piedra" and eleccion_computadora == "tijera") or \
             (eleccion_jugador == "papel" and eleccion_computadora == "piedra") or \
             (eleccion_jugador == "tijera" and eleccion_computadora == "papel"):
            print("¡Ganaste esta ronda!")
            puntaje_jugador += 1
        else:
            print("¡Perdiste esta ronda!")
            puntaje_computadora += 1
        
        print(f"Puntaje - Jugador: {puntaje_jugador}, Computadora: {puntaje_computadora}")

# Ejecutar el juego
jugar()
