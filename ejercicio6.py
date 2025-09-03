def encontrar_indices(frase, letra):
    """
    Función que busca todas las posiciones de una letra dentro de una frase.
    Uso enumerate() para obtener tanto el índice como el carácter.
    Devuelve una lista con los índices donde aparece la letra.
    """

    # 1) Inicializo una lista vacía para guardar las posiciones encontradas
    posiciones = []

    # 2) Recorro la frase con enumerate(), que me da (índice, caracter)
    for indice, caracter in enumerate(frase):
        # 3) Comparo el caracter actual con la letra buscada
        if caracter.lower() == letra.lower():
            # Si son iguales (ignoro mayúsculas/minúsculas), guardo el índice
            posiciones.append(indice)
    # 4) Devuelvo la lista con todas las posiciones encontradas
    return posiciones


# 5) Ejemplo de uso:
frase = "Hola SENA"
letra = "a"
resultado = encontrar_indices(frase, letra)
print(f"La letra '{letra}' aparece en las posiciones: {resultado}")
