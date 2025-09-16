import random

def simulador_dados(n_lanzamientos=10000):
    """
    Simula el lanzamiento de dos dados n_lanzamientos veces.
    - Cada dado genera un número aleatorio entre 1 y 6.
    - Calcula la suma de los dos dados.
    - Devuelve un diccionario con la frecuencia de cada suma (2 a 12).
    """
    frecuencias = {}

    for _ in range(n_lanzamientos):
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        total = dado1 + dado2
        frecuencias[total] = frecuencias.get(total, 0) + 1

    return frecuencias  # devuelve un diccionario

# Si se ejecuta directamente, imprime los resultados
if __name__ == "__main__":
    resultado = simulador_dados()
    print("=== Frecuencia de cada suma (10,000 lanzamientos) ===")
    for suma in range(2, 13):  # posibles valores entre 2 y 12
        print(f"Suma {suma}: {resultado.get(suma, 0)} veces")
