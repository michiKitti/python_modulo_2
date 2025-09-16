def validar_indice_letras(frase: str, letra: str) -> list[int]:
    """
    Busca todas las posiciones de una letra dentro de una frase.
    Devuelve una lista con los índices donde aparece la letra,
    ignorando mayúsculas/minúsculas.
    """
    posiciones = []
    for indice, character in enumerate(frase):
        if character.lower() == letra.lower():
            posiciones.append(indice)
    return posiciones


def validar_indice():
    """
    Función interactiva que pide al usuario una frase y una letra.
    Devuelve la lista de posiciones donde aparece la letra.
    """
    frase = input("Ingresa una frase: ")
    letra = input("Ingresa una letra a buscar: ")
    resultado = validar_indice_letras(frase, letra)
    print(f"La letra '{letra}' aparece en las posiciones: {resultado}")
    return resultado  # devolvemos para poder testearlo en las pruebas
