def aplicar_iva():
    """
    Tengo una lista de productos (cada producto es un diccionario con nombre y precio).
    Quiero crear un nuevo diccionario usando dictionary comprehension:
      - Claves  = nombres de los productos
      - Valores = precios con IVA del 19% incluido
    """

    # 1) Lista inicial de productos
    productos = [
        {"nombre": "Camisa", "precio": 50000},
        {"nombre": "Pantalón", "precio": 80000}
    ]

    # 2) Dictionary comprehension para calcular el precio con IVA
    productos_con_iva = {
        producto["nombre"]: round(producto["precio"] * 1.19, 2)  # precio con 19% de IVA
        for producto in productos
    }

    # 3) Muestro el resultado
    print("Diccionario con precios + IVA:")
    print(productos_con_iva)

    # 4) Devuelvo el diccionario por si lo quiero usar después
    return productos_con_iva


# 5) Llamo a la función
aplicar_iva()
