def aventura_texto():
    """
    Juego de aventura en texto:
    - El jugador empieza en la habitación inicial.
    - Puede tomar decisiones escribiendo comandos.
    - Hay 3 habitaciones y un final (ganar o perder).
    """

    # 1) Defino la habitación inicial
    habitacion = "inicio"
    juego_activo = True  # para controlar el bucle principal

    print("¡Bienvenido a la Aventura del Tesoro!")
    print("Estás en una habitación oscura. Solo ves una puerta al norte.")

    # 2) Bucle principal del juego
    while juego_activo:
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
                print("¡Increíble! Venciste al monstruo y encuentras el tesoro. ")
                print("¡Has ganado la aventura!")
                juego_activo = False
            elif accion == "huir":
                print("Intentas huir, pero el monstruo te atrapa.")
                print("Fin del juego. Has perdido.")
                juego_activo = False
            else:
                print("Debes elegir: 'luchar' o 'huir'.")

    print("\nGracias por jugar.")

# Llamo a la función para ejecutar el juego
aventura_texto()
