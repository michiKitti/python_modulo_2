import unittest
from unittest.mock import patch
import io

from ejercicio7 import validar_combinador_listas, validar_variables


class TestValidarCombinadorListas(unittest.TestCase):

    def test_combinador_basico(self):
        """Prueba con dos elementos en cada lista."""
        nombres = ["Ana", "Carlos"]
        notas = [4.5, 3.8]
        esperado = {"Ana": 4.5, "Carlos": 3.8}
        self.assertEqual(validar_combinador_listas(nombres, notas), esperado)

    def test_listas_desiguales(self):
        """Prueba con listas de distinta longitud."""
        nombres = ["Ana", "Carlos", "Luis"]
        notas = [4.5]
        esperado = {"Ana": 4.5}  # zip se detiene en el más corto
        self.assertEqual(validar_combinador_listas(nombres, notas), esperado)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_validar_variables(self, mock_stdout):
        """Prueba que la función imprimir variables saca el texto esperado."""
        estudiantes = {"Ana": 4.5, "Carlos": 3.8}
        validar_variables(estudiantes)
        salida = mock_stdout.getvalue()
        self.assertIn("El estudiante Ana tiene una nota de 4.5", salida)
        self.assertIn("El estudiante Carlos tiene una nota de 3.8", salida)


if __name__ == "__main__":
    unittest.main()
