def clasificador_numeros():
    """
    Programa que clasifica un número como Par o Impar usando un operador ternario.
    Además, si el número es múltiplo de 5, muestra un mensaje extra.
    """

    # 1) Pido un número al usuario y lo convierto a entero
    numero = int(input("Ingresa un número: "))

    # 2) Uso el operador ternario para decidir si es Par o Impar
    #    Sintaxis: valor_si_verdadero if condicion else valor_si_falso
    resultado = "Par" if numero % 2 == 0 else "Impar"

    # 3) Muestro el resultado
    print(f"El número {numero} es {resultado}.")

    # 4) Ahora reviso si es múltiplo de 5 con el operador módulo
    if numero % 5 == 0:
        print("Además, el número es múltiplo de 5.")

# 5) Llamo a la función
clasificador_numeros()
