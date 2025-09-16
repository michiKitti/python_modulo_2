import unittest
from unittest.mock import patch
from io import StringIO

from ejercicio3 import validar_contrasena


class TestValidarContrasena(unittest.TestCase):

    def test_contrasena_valida(self):
        with patch("builtins.input", side_effect=["Valery123"]), \
             patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            validar_contrasena()
            salida = mock_stdout.getvalue()
            self.assertIn("✅ Contraseña creada con éxito.", salida)

    def test_contrasena_corta(self):
        with patch("builtins.input", side_effect=["abc", "Valery123"]), \
             patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            validar_contrasena()
            salida = mock_stdout.getvalue()
            self.assertIn("La contraseña debe tener al menos 8 caracteres.", salida)
            self.assertIn("✅ Contraseña creada con éxito.", salida)

    def test_sin_mayuscula(self):
        with patch("builtins.input", side_effect=["valery123", "Valery123"]), \
             patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            validar_contrasena()
            salida = mock_stdout.getvalue()
            self.assertIn("La contraseña debe contener al menos una letra mayúscula.", salida)
            self.assertIn("✅ Contraseña creada con éxito.", salida)

    def test_sin_numero(self):
        with patch("builtins.input", side_effect=["Valeryyyy", "Valery123"]), \
             patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            validar_contrasena()
            salida = mock_stdout.getvalue()
            self.assertIn("La contraseña debe contener al menos un número.", salida)
            self.assertIn("✅ Contraseña creada con éxito.", salida)


if __name__ == "__main__":
    unittest.main()
