"""Juego de Piedra, Papel o Tijeras
Implementa el clásico juego para jugar contra la computadora.
•	El usuario elige una opción y la computadora elige una al azar.
•	El programa determina el ganador basándose en las reglas (piedra vence a tijeras, tijeras a papel, papel a piedra).
•	Se debe llevar un conteo de las victorias del jugador y de la computadora. El juego termina cuando uno de los dos llegue a 3 victorias.
Conceptos aplicados: random.choice(), bucle while, if/elif/else, contadores, f-strings.
"""
import random

def juego_piedra_papel_tijeras():
    """
    Juego clásico de Piedra, Papel o Tijeras contra la computadora.
    Reglas:
    - Piedra gana a Tijeras
    - Tijeras gana a Papel
    - Papel gana a Piedra
    El primero que llegue a 3 victorias gana la partida.
    """

    # 1) Inicializo los contadores de victorias
    victorias_jugador = 0
    victorias_pc = 0

    # 2) Opciones disponibles
    opciones = ["piedra", "papel", "tijeras"]

    print("=== Juego: Piedra, Papel o Tijeras ===")
    print("El primero en llegar a 3 victorias gana la partida.\n")

    # 3) El juego se repite hasta que alguien llegue a 3 victorias
    while victorias_jugador < 3 and victorias_pc < 3:
        # 4) Pido al jugador su elección
        jugador = input("Elige piedra, papel o tijeras: ").lower()

        # 5) Valido que sea una opción válida
        if jugador not in opciones:
            continue  # vuelve al inicio del bucle

        # 6) La computadora elige una opción al azar
        pc = random.choice(opciones)
        print(f"La computadora eligió: {pc}")

        # 7) Comparo las elecciones y determino el ganador de la ronda
        if jugador == pc:
        elif (jugador == "piedra" and pc == "tijeras") or \
             (jugador == "tijeras" and pc == "papel") or \
             (jugador == "papel" and pc == "piedra"):
            victorias_jugador += 1
        else:
            victorias_pc += 1

        # 8) Muestro el marcador actual
        print(f"Marcador: Tú {victorias_jugador} - {victorias_pc} Computadora\n")

    # 9) Al salir del bucle, alguien llegó a 3 victorias
    if victorias_jugador == 3:
    else:

# 10) Llamo a la función para jugar
juego_piedra_papel_tijeras()
