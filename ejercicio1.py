def sistema_precios_cine():
    """
    Este programa calcula el precio de una entrada de cine según la edad
    y aplica un 10% de descuento si la persona es estudiante.
    """

def validar_estudiante(estudiante, precio):
    if estudiante == "si":
        precio = precio * 0.9  # descuento del 10%
    return precio

def validar_edad(edad):
    if edad < 12:
        precio = 10000
    elif 12 <= edad <= 17:
        precio = 15000
    else:
        precio = 20000
    return precio

def main():
    edad = int(input("Ingrese su edad: "))  # convertir a int
    precio = validar_edad(edad)  # guardar resultado
    estudiante = input("¿Es estudiante? (si/no): ").lower()
    precio_final = validar_estudiante(estudiante, precio)  # aplicar descuento si corresponde
    print(f"El precio de la entrada es: {precio_final}")

if __name__ == "__main__":
    main()

