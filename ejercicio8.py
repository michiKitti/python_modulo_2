def filtrado_datos():
    """
    Trabajo con list comprehensions:
    - Genera lista de números positivos
    - Genera lista de cuadrados
    - Genera lista de strings "positivo"/"negativo"
    """
    # 1) Lista inicial
    numeros = [-5, 10, -15, 20, -25, 30]

    # 2) Lista con solo los números positivos
    positivos = [n for n in numeros if n > 0]

    # 3) Lista con los cuadrados de todos los números
    cuadrados = [n ** 2 for n in numeros]

    # 4) Lista de strings usando un ternario
    etiquetas = ["positivo" if n > 0 else "negativo" for n in numeros]

    # 5) Imprimo resultados usando la función auxiliar
    validar_datos(cuadrados, etiquetas, positivos)

    # 6) Devuelvo los resultados para poder testear
    return positivos, cuadrados, etiquetas


def validar_datos(cuadrados, etiquetas, positivos):
    """
    Imprime los resultados en pantalla.
    """
    print("Números positivos:", positivos)
    print("Cuadrados de todos los números:", cuadrados)
    print("Etiquetas positivo/negativo:", etiquetas)


if __name__ == "__main__":
    filtrado_datos()
