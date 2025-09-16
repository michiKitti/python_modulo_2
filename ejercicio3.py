def validar_contrasena():
    """
    Intérprete de validación de contraseñas.
    Pide al usuario crear una contraseña hasta que cumpla TODAS las reglas:
    - Mínimo 8 caracteres.
    - Al menos una letra mayúscula.
    - Al menos un número.

    Si falla, muestra qué regla no se cumplió y vuelve a pedirla.
    """
    while True:
        contrasena = input("Crea una contraseña: ")
        errores = []

        # Regla 1: longitud mínima
        if len(contrasena) < 8:
            errores.append("La contraseña debe tener al menos 8 caracteres.")

        # Regla 2: al menos una mayúscula
        if not any(c.isupper() for c in contrasena):
            errores.append("La contraseña debe contener al menos una letra mayúscula.")

        # Regla 3: al menos un número
        if not any(c.isdigit() for c in contrasena):
            errores.append("La contraseña debe contener al menos un número.")

        # Si no hay errores → contraseña válida
        if not errores:
            print("✅ Contraseña creada con éxito.")
            break
        else:
            for error in errores:
                print("-", error)
            print()  # línea en blanco para separar intentos


if __name__ == "__main__":
    validar_contrasena()


def juego_piedra_papel_tijeras():
    return None