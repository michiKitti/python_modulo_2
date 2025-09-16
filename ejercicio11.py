def validar_cedula(numero_cedula):
    """
    Válida una cédula con una regla simple:
    - Sumo todos los dígitos de la cédula.
    - Si la suma es par, la cédula es válida → devuelve True.
    - Si la suma es impar, la cédula no es válida → devuelve False.
    """
    suma = 0
    for digito in numero_cedula:
        suma += int(digito)
    return suma % 2 == 0  # True si es par, False si no


# --- Programa principal ---
if __name__ == "__main__":
    while True:
        cedula_ingresada = input("Ingrese su número de cédula: ")
        if validar_cedula(cedula_ingresada):
            print("Cédula válida")
            break
        else:
            print("Cédula no válida, inténtelo de nuevo.\n")
