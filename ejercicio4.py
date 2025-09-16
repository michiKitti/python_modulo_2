import random

def determinar_ganador(jugador, pc):
    """
    Determina el resultado de una ronda.
    Retorna:
    - "jugador" si gana el jugador
    - "pc" si gana la computadora
    - "empate" si ambos eligen lo mismo
    """
    if jugador == pc:
        return "empate"
    elif (jugador == "piedra" and pc == "tijeras") or \
         (jugador == "tijeras" and pc == "papel") or \
         (jugador == "papel" and pc == "piedra"):
        return "jugador"
    else:
        return "pc"


def jugar_ronda(jugador, pc):


        """
        Devuelve el mensaje de la ronda y el ganador.
        """
        if jugador not in ["piedra", "papel", "tijeras"]:
            return "Opción no válida.", None

        ganador = determinar_ganador(jugador, pc)

        if ganador == "empate":
            return "Empate, nadie gana esta ronda.", "empate"
        elif ganador == "jugador":
            return "¡Ganaste esta ronda!", "jugador"
        else:
            return "La computadora gana esta ronda.", "pc"


def juego_piedra_papel_tijeras():

        """
        Juego principal contra la computadora (con input/print).
        El primero que llega a 3 victorias gana.
        """
        victorias_jugador = 0
        victorias_pc = 0
        opciones = ["piedra", "papel", "tijeras"]

        print("=== Juego: Piedra, Papel o Tijeras ===")
        print("El primero en llegar a 3 victorias gana la partida.\n")

        while victorias_jugador < 3 and victorias_pc < 3:
            jugador = input("Elige piedra, papel o tijeras: ").lower()
            pc = random.choice(opciones)
            print(f"La computadora eligió: {pc}")

            mensaje, ganador = jugar_ronda(jugador, pc)
            print(mensaje + "\n")

            if ganador == "jugador":
                victorias_jugador += 1
            elif ganador == "pc":
                victorias_pc += 1

        if victorias_jugador == 3:
            print("¡Felicidades! Ganaste la partida.")
        else:
            print("La computadora ganó la partida.")


if __name__ == "__main__":
    juego_piedra_papel_tijeras()
