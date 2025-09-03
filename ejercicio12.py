import random

def simulador_dados():
    """
    Simula el lanzamiento de dos dados 10,000 veces.
    - Cada dado genera un número aleatorio entre 1 y 6.
    - Calculo la suma de los dos dados.
    - Uso un diccionario para contar cuántas veces aparece cada suma (2 a 12).
    """

    # 1) Inicializo un diccionario vacío para los conteos
    frecuencias = {}

    # 2) Hago 10,000 lanzamientos
    for _ in range(10000):
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        suma = dado1 + dado2

        # 3) Incremento el contador en el diccionario
        #    Si la clave no existe, uso get() para empezar en 0
        frecuencias[suma] = frecuencias.get(suma, 0) + 1

    # 4) Imprimo el reporte ordenado de menor a mayor suma
    print("=== Frecuencia de cada suma (10,000 lanzamientos) ===")
    for suma in range(2, 13):  # posibles valores entre 2 y 12
        print(f"Suma {suma}: {frecuencias.get(suma, 0)} veces")


# 5) Llamo a la función
simulador_dados()
