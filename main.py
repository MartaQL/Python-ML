print('Hello world')


import random

def obtener_movimiento_jugador():
    """Esta función permite al jugador elegir su movimiento."""
    while True:
        jugador = input("Elige piedra, papel o tijeras: ").lower()
        if jugador in ["piedra", "papel", "tijeras"]:
            return jugador
        else:
            print("Por favor, elige una opción válida.")

def obtener_movimiento_computadora():
    """Esta función genera aleatoriamente el movimiento de la computadora."""
    return random.choice(["piedra", "papel", "tijeras"])

def determinar_ganador(jugador, computadora):
    """Esta función determina quién gana el juego."""
    if jugador == computadora:
        return "Empate"
    elif (jugador == "piedra" and computadora == "tijeras") or \
         (jugador == "papel" and computadora == "piedra") or \
         (jugador == "tijeras" and computadora == "papel"):
        return "¡Ganaste!"
    else:
        return "¡La computadora gana!"

def jugar_piedra_papel_tijeras():
    """Esta función ejecuta el juego piedra, papel o tijeras."""
    print("¡Bienvenido al juego de Piedra, Papel o Tijeras!")
    while True:
        jugador = obtener_movimiento_jugador()
        computadora = obtener_movimiento_computadora()
        print(f"Tú elegiste: {jugador}")
        print(f"La computadora eligió: {computadora}")
        resultado = determinar_ganador(jugador, computadora)
        print(resultado)
        jugar_nuevamente = input("¿Quieres jugar de nuevo? (sí/no): ").lower()
        if jugar_nuevamente != "sí":
            print("¡Gracias por jugar!")
            break

# Para iniciar el juego, llama a la función jugar_piedra_papel_tijeras()
jugar_piedra_papel_tijeras()