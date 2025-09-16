def validar_clasificador_de_numeros():

        """
        Clasifica un número como Par o Impar usando un operador ternario.
        Además, si el número es múltiplo de 5, incluye un mensaje adicional.
        """
        # Uso del operador ternario
        resultado = "Par" if numero % 2 == 0 else "Impar"

        # Construyo el mensaje base
        mensaje = f"El número {numero} es {resultado}."

        # Verifico si es múltiplo de 5
        if numero % 5 == 0:
            mensaje += " Además, el número es múltiplo de 5."

        return mensaje



# Ejemplo de uso interactivo (no necesario para las pruebas)
if __name__ == "__main__":
   numero = int(input("Ingresa un número: "))
validar_clasificador_de_numeros()
