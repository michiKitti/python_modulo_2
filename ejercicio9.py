def filtrado_datos():
    """
    Genera tres listas a partir de una lista inicial:
    - Números positivos
    - Cuadrados de todos los números
    - Etiquetas "positivo"/"negativo"
    Devuelve las tres listas en un diccionario para facilitar las pruebas.
    """
    # Lista inicial
    numeros = [-5, 10, -15, 20, -25, 30]

    # 1) Lista con solo los números positivos
    positivos = [n for n in numeros if n > 0]

    # 2) Lista con los cuadrados de todos los números
    cuadrados = [n ** 2 for n in numeros]

    # 3) Lista de strings usando un ternario
    etiquetas = ["positivo" if n > 0 else "negativo" for n in numeros]

    # ✅ Devuelvo los resultados para poder testear
    return {
        "positivos": positivos,
        "cuadrados": cuadrados,
        "etiquetas": etiquetas,
    }


def imprimir_datos(datos):
    """
    Recibe el diccionario devuelto por filtrado_datos() y lo imprime.
    """
    print("Números positivos:", datos["positivos"])
    print("Cuadrados de todos los números:", datos["cuadrados"])
    print("Etiquetas positivo/negativo:", datos["etiquetas"])


# Ejemplo de uso interactivo
if __name__ == "__main__":
    resultados = filtrado_datos()
    imprimir_datos(resultados)
