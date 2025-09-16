def interprete_comandos():
    """
    Intérprete de Comandos Sencillo
    Simula un menú de consola con los comandos:
    - "guardar" → imprime "Guardando archivo..."
    - "cargar" → imprime "Cargando archivo..."
    - "salir" → finaliza el programa
    Si el comando no es válido, muestra un mensaje de error.
    """
    while True:
        comando = input("Ingresa un comando: ").lower()

        match comando:
            case "guardar":
                print("Guardando archivo...")
            case "cargar":
                print("Cargando archivo...")
            case "salir":
                print("Saliendo del programa. ¡Adiós!")
                break
            case _:
                print("Error: comando no reconocido. Intenta de nuevo.")

def validar_comandos(self, mock_stdout, mock_input):
        interprete_comandos()
        salida = mock_stdout.getvalue()
        self.assertIn("Guardando archivo...", salida)
        self.assertIn("Saliendo del programa. ¡Adiós!", salida)
        mock_input.assert_called()  # <-- así ya PyCharm reconoce que se usa

        interprete_comandos()
        salida = mock_stdout.getvalue()
        self.assertIn("Guardando archivo...", salida)
        self.assertIn("Saliendo del programa. ¡Adiós!", salida)
        mock_input.assert_called()  # <-- así ya PyCharm reconoce que se usa


# Ejecutar el intérprete solo si el archivo es ejecutado directamente
if __name__ == "__main__":
    interprete_comandos()
