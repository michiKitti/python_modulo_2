import random

def mostrar_tablero(palabra_secreta, letras_adivinadas, vidas):
    """
    Muestra el estado actual del tablero:
    - Letras adivinadas o guiones bajos
    - Letras ya intentadas
    - Vidas restantes
    """
    tablero = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            tablero += letra + " "
        else:
            tablero += "_ "
    print("\nPalabra: ", tablero)
    print("Letras usadas:", " ".join(sorted(letras_adivinadas)))
    print(f"Vidas restantes: {vidas}")


def validar_entrada(letra, letras_adivinadas):
    """
    Válida que la entrada:
    - Sea una sola letra
    - No se haya intentado antes
    """
    if len(letra) != 1 or not letra.isalpha():
        print(" Ingresa solo una letra válida.")
        return False
    if letra in letras_adivinadas:
        print("Ya intentaste esa letra.")
        return False
    return True


def jugar_ahorcado():
    """
    Juego principal del Ahorcado:
    - Escoge palabra al azar
    - Controla vidas, tablero y estado del juego
    """
    # Lista de palabras secretas
    palabras = ["python", "computadora", "teclado", "programación", "ahorcado"]
    palabra_secreta = random.choice(palabras)

    vidas = 6  # número de intentos permitidos
    letras_adivinadas = set()  # letras que el jugador ya intentó
    letras_correctas = set(palabra_secreta)  # letras que debo adivinar

    print(" Bienvenido al Juego del Ahorcado ")
    print("Adivina la palabra secreta... ¡Tienes 6 vidas!")

    # Bucle principal
    while vidas > 0 and not letras_correctas.issubset(letras_adivinadas):
        mostrar_tablero(palabra_secreta, letras_adivinadas, vidas)

        # Pedir letra
        intento = input("Ingresa una letra: ").lower()

        # Validar entrada
        if not validar_entrada(intento, letras_adivinadas):
            continue

        # Agregar letra a las intentadas
        letras_adivinadas.add(intento)

        # Revisar si la letra está en la palabra
        if intento in palabra_secreta:
            print(f" ¡Bien! La letra '{intento}' está en la palabra.")
        else:
            vidas -= 1
            print(f"La letra '{intento}' no está. Pierdes una vida.")

    # Fin del juego
    if letras_correctas.issubset(letras_adivinadas):
        print(f"\n ¡Ganaste! La palabra era: {palabra_secreta}")
    else:
        print(f"\n Perdiste. La palabra era: {palabra_secreta}")


# Llamar al juego
jugar_ahorcado()
