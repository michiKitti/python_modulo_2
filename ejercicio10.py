def transponer_matriz(matriz):
    """
    Recibe una matriz (lista de listas) y devuelve su transpuesta.
    Versión usando bucles for anidados.
    """
    # Número de filas y columnas originales
    filas = len(matriz)
    columnas = len(matriz[0])

    # Creo una lista vacía para la transpuesta
    transpuesta = []

    # Recorro las columnas de la matriz original
    for c in range(columnas):
        nueva_fila = []
        # Recorro las filas de la matriz original
        for f in range(filas):
            nueva_fila.append(matriz[f][c])
        # Agrego la nueva fila a la transpuesta
        transpuesta.append(nueva_fila)

    return transpuesta


def transponer_matriz_refactor(matriz):
    """
    Recibe una matriz (lista de listas) y devuelve su transpuesta.
    Versión usando list comprehension.
    """
    return [[fila[c] for fila in matriz] for c in range(len(matriz[0]))]


# Ejemplo solo si se ejecuta directamente este archivo
if __name__ == "__main__":
    m = [[1, 2, 3], [4, 5, 6]]
    print("Original:", m)
    print("Transpuesta (básica):", transponer_matriz(m))
    print("Transpuesta (refactor):", transponer_matriz_refactor(m))
