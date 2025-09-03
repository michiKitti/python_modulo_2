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


# Ejemplo
m = [[1, 2, 3], [4, 5, 6]]
print("Original:", m)
print("Transpuesta:", transponer_matriz(m))
