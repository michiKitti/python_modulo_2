def aventura_texto(comandos=None):
    """
    Juego de aventura en texto.
    - El jugador empieza en la habitación inicial.
    - Puede tomar decisiones escribiendo comandos.
    - Hay 3 habitaciones y un final (ganar o perder).
    Si se pasa una lista en 'comandos', se usan esos comandos en vez de input().
    Devuelve "ganaste" o "perdiste".
    """

    habitacion = "inicio"
    juego_activo = True
    resultado = None  # para devolver al final

    print("¡Bienvenido a la Aventura del Tesoro!")
    print("Estás en una habitación oscura. Solo ves una puerta al norte.")

    # para pruebas unitarias: iterador de comandos
    comandos_iter = iter(comandos) if comandos is not None else None

    while juego_activo:
        # pedir acción
        if comandos_iter:
            try:
                accion = next(comandos_iter).lower()
                print(f"> {accion}")  # muestra el comando simulado
            except StopIteration:
                break
        else:
            accion = input("\n¿Qué quieres hacer? > ").lower()

        # --- HABITACIÓN INICIO ---
        if habitacion == "inicio":
            if accion == "ir al norte":
                print("Caminas hacia el norte y llegas a la sala del cofre.")
                habitacion = "cofre"
            else:
                print("No entiendo ese comando. Intenta con 'ir al norte'.")

        # --- HABITACIÓN DEL COFRE ---
        elif habitacion == "cofre":
            if accion == "abrir cofre":
                print("¡Oh no! El cofre estaba maldito y aparece un monstruo. 🐉")
                habitacion = "monstruo"
            elif accion == "ir al sur":
                print("Regresas a la habitación inicial.")
                habitacion = "inicio"
            else:
                print("Comando inválido. Opciones: 'abrir cofre' o 'ir al sur'.")

        # --- HABITACIÓN DEL MONSTRUO ---
        elif habitacion == "monstruo":
            if accion == "luchar":
                print("¡Increíble! Venciste al monstruo y encuentras el tesoro.")
                print("¡Has ganado la aventura!")
                resultado = "ganaste"
                juego_activo = False
            elif accion == "huir":
                print("Intentas huir, pero el monstruo te atrapa.")
                print("Fin del juego. Has perdido.")
                resultado = "perdiste"
                juego_activo = False
            else:
                print("Debes elegir: 'luchar' o 'huir'.")

    print("\nGracias por jugar.")
    return resultado  # útil para tests


if __name__ == "__main__":
    aventura_texto()  # modo interactivo
