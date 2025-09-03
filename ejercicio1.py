def sistema_precios_cine():
    """
    Este programa calcula el precio de una entrada de cine según la edad
    y aplica un 10% de descuento si la persona es estudiante.
    """

    # 1) Pedir datos al usuario
    edad = int(input("Ingrese su edad: "))
    estudiante = input("¿Es estudiante? (si/no): ").lower()

    # 2) Determinar precio base según la edad
    if edad < 12:
        precio = 10000
    elif edad <= 17:  # entre 12 y 17
        precio = 15000
    else:  # 18 en adelante
        precio = 20000

    # 3) Aplicar descuento si es estudiante
    if estudiante == "si":
        precio = precio * 0.9  # descuento del 10%

    # 4) Mostrar resultado
    print(f"El precio de la entrada es: ${precio:,.0f}")


# 5) Llamar a la función
sistema_precios_cine()
