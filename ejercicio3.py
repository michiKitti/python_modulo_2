"""Escribe un programa que pida al usuario crear una contraseña y la valide usando un bucle while. El bucle solo terminará cuando la contraseña cumpla todos los criterios:
•	Mínimo 8 caracteres de longitud.
•	Contiene al menos una letra mayúscula.
•	Contiene al menos un número.
•	En cada intento fallido, el programa debe indicar qué regla no se cumplió
"""
def validar_contrasena():
    """
    Mis apuntes:
    - Voy a pedir una contraseña hasta que cumpla TODAS las reglas.
    - Reglas: mínimo 8 caracteres, al menos una mayúscula y al menos un número.
    - Si no cumple, le muestro al usuario qué le faltó y vuelvo a pedirla.
    """

    # Uso un bucle infinito porque solo salgo cuando la contraseña es válida.
    while True:
        # 1) Pido la contraseña al usuario
        contrasena = input("Crea una contraseña: ")

        # 2) Aquí voy a guardar los mensajes de error de las reglas que no se cumplan
        errores = []

        # 3) Reviso la longitud: debe tener 8 o más caracteres
        if len(contrasena) < 8:
            errores.append("La contraseña debe tener al menos 8 caracteres.")

        # 4) Reviso si tiene al menos una letra mayúscula.
        #    Uso 'any' para chequear si existe al menos un carácter que cumpla isupper()
        tiene_mayuscula = any(c.isupper() for c in contrasena)
        if not tiene_mayuscula:
            errores.append("La contraseña debe contener al menos una letra mayúscula.")

        # 5) Reviso si tiene al menos un número.
        #    Igual que arriba, 'any' + isdigit() para ver si hay algún dígito.
        tiene_numero = any(c.isdigit() for c in contrasena)
        if not tiene_numero:
            errores.append("La contraseña debe contener al menos un número.")

        # 6) Si la lista de errores está vacía, es porque pasó todas las validaciones
        if not errores:
            # Salgo del while porque ya terminé
            break
        else:
            # 7) Si hubo errores, los imprimo todos para que el usuario sepa qué corregir
            for error in errores:
                print("-", error)
            # 8) Dejo una línea en blanco para separar visualmente los intentos
            print()

# 9) Llamo a la función para ejecutar mi programa
validar_contrasena()
