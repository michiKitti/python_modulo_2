def validar_combinador_listas(nombres: list[str], notas: list[float]) -> dict[str, float]:
    """
    Función que recibe dos listas: una de nombres y otra de notas.
    Combina ambas listas usando zip() para crear un diccionario donde:
    - Claves = nombres de estudiantes
    - Valores = notas finales
    Devuelve el diccionario resultante.
    """
    estudiantes = dict(zip(nombres, notas))
    return estudiantes  # devolvemos para poder usarlo/testearlo


def validar_variables(estudiantes: dict[str, float]) -> None:

    for nombre, nota in estudiantes.items():
        print(f"El estudiante {nombre} tiene una nota de {nota}")


if __name__ == "__main__":
    # Ejemplo de uso:
    lista_nombres = ["Ana", "Carlos", "María", "Luis"]
    lista_notas = [4.5, 3.8, 4.9, 3.2]

    resultado = validar_combinador_listas(lista_nombres, lista_notas)
    validar_variables(resultado)
