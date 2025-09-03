import random

# ---------------- FUNCIONES ----------------
def crear_tablero(tamaño=5):
    """Creo un tablero vacío (lista de listas) con guiones para representar el mar."""
    return [["~" for _ in range(tamaño)] for _ in range(tamaño)]


def imprimir_tablero(tablero):
    """Muestro el tablero con coordenadas (A-E para filas, 1-5 para columnas)."""
    print("\n   1  2  3  4  5")
    letras = "ABCDE"
    for i, fila in enumerate(tablero):
        print(letras[i], " ".join(fila))


def colocar_barco(tamaño=5, longitud=3):
    """
    Escondo un barco de longitud dada en el tablero:
    - Puede estar en una fila o en una columna.
    - Devuelvo una lista con las coordenadas [(fila, col), ...].
    """
    orientacion = random.choice(["horizontal", "vertical"])
    if orientacion == "horizontal":
        fila = random.randint(0, tamaño - 1)
        col = random.randint(0, tamaño - longitud)
        return [(fila, col + i) for i in range(longitud)]
    else:
        fila = random.randint(0, tamaño - longitud)
        col = random.randint(0, tamaño - 1)
        return [(fila + i, col) for i in range(longitud)]


def validar_entrada(entrada):
    """Valido que la coordenada sea correcta, ej: A3, B5..."""
    if len(entrada) != 2:
        return None
    fila_letra, col_str = entrada[0].upper(), entrada[1]
    if fila_letra not in "ABCDE" or not col_str.isdigit():
        return None
    fila = "ABCDE".index(fila_letra)
    col = int(col_str) - 1
    if 0 <= fila < 5 and 0 <= col < 5:
        return (fila, col)
    return None


# ---------------- JUEGO PRINCIPAL ----------------
def jugar_batalla_naval():
    print("Bienvenido a Batalla Naval Simplificada ")
    tablero = crear_tablero()
    barco = colocar_barco()
    intentos = 10
    aciertos = []

    # Bucle principal
    while intentos > 0 and len(aciertos) < len(barco):
        imprimir_tablero(tablero)
        print(f"\nTe quedan {intentos} intentos.")

        # Pedir coordenada
        entrada = input("Dispara (ejemplo A3): ").strip()
        coordenada = validar_entrada(entrada)

        if not coordenada:
            print("Entrada inválida. Usa formato (A-E)(1-5), ejemplo: B4.")
            continue

        if coordenada in aciertos:
            print(" Ya habías acertado aquí.")
            continue

        fila, col = coordenada

        # Revisar si acertó en el barco
        if coordenada in barco:
            print(" ¡Tocado!")
            tablero[fila][col] = "X"
            aciertos.append(coordenada)
        else:
            print("Agua...")
            tablero[fila][col] = "O"

        intentos -= 1

    # Fin del juego
    imprimir_tablero(tablero)
    if len(aciertos) == len(barco):
        print("\n ¡Hundiste el barco completo! ¡Ganaste!")
    else:
        print("\n Se acabaron tus intentos. Perdiste.")
        print("El barco estaba en:", barco)


# ---------------- EJECUCIÓN ----------------
jugar_batalla_naval()
