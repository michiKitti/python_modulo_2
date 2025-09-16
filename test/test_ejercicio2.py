import unittest
from unittest.mock import patch
from io import StringIO

from ejercicio2 import interprete_comandos


class TestInterpreteComandos(unittest.TestCase):

    def test_guardar_y_salir(self):
        with patch("builtins.input", side_effect=["guardar", "salir"]), \
             patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            interprete_comandos()
            salida = mock_stdout.getvalue()
            self.assertIn("Guardando archivo...", salida)
            self.assertIn("Saliendo del programa. ¡Adiós!", salida)

    def test_cargar_y_salir(self):
        with patch("builtins.input", side_effect=["cargar", "salir"]), \
             patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            interprete_comandos()
            salida = mock_stdout.getvalue()
            self.assertIn("Cargando archivo...", salida)
            self.assertIn("Saliendo del programa. ¡Adiós!", salida)

    def test_comando_invalido(self):
        with patch("builtins.input", side_effect=["xyz", "salir"]), \
             patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            interprete_comandos()
            salida = mock_stdout.getvalue()
            self.assertIn("Error: comando no reconocido. Intenta de nuevo.", salida)
            self.assertIn("Saliendo del programa. ¡Adiós!", salida)


if __name__ == "__main__":
    unittest.main()
