def validar_cedula(cedula):
    """
    Valida una cédula con una regla simple:
    - Sumo todos los dígitos de la cédula.
    - Si la suma es par, la cédula es válida → devuelve True.
    - Si la suma es impar, la cédula no es válida → devuelve False.
    """

    # 1) Inicializo la suma en 0
    suma = 0

    # 2) Recorro cada carácter de la cédula (que es un string)
    for digito in cedula:
        # 3) Convierto el carácter a entero y lo voy sumando
        suma += int(digito)

    # 4) Reviso si la suma es par o impar
    return suma % 2 == 0   # True si es par, False si no


# --- Programa principal ---
while True:
    # 5) Pido la cédula al usuario
    cedula = input("Ingrese su número de cédula: ")

    # 6) Valido con mi función
    if validar_cedula(cedula):
        print("Cédula válida")
        break   # salgo del bucle porque ya es válida
    else:
        print("Cédula no válida, inténtelo de nuevo.\n")
