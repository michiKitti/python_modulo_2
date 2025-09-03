def combinador_listas(nombres, notas):
    """
    Función que recibe dos listas: una de nombres y otra de notas.
    Combina ambas listas usando zip() para crear un diccionario donde:
    - Claves = nombres de estudiantes
    - Valores = notas finales
    Luego imprime un reporte con los resultados.
    """

    # 1) Combino las dos listas en pares (nombre, nota) con zip()
    #    Después las paso a dict() para obtener un diccionario
    estudiantes = dict(zip(nombres, notas))

    # 2) Recorro el diccionario con un for
    for nombre, nota in estudiantes.items():
        # 3) Imprimo el reporte con f-string
        print(f"El estudiante {nombre} tiene una nota de {nota}")

    # 4) Devuelvo el diccionario por si quiero usarlo más adelante
    return estudiantes


# 5) Ejemplo de uso:
lista_nombres = ["Ana", "Carlos", "María", "Luis"]
lista_notas = [4.5, 3.8, 4.9, 3.2]

resultado = combinador_listas(lista_nombres, lista_notas)
