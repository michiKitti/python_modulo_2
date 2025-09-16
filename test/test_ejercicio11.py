import unittest
from ejercicio11 import validar_cedula

class TestValidarCedula(unittest.TestCase):
    def test_cedula_valida(self):
        # suma 1+2+3+4 = 10 (par)
        self.assertTrue(validar_cedula("1234"))

    def test_cedula_no_valida(self):
        # suma 1+2+3+5 = 11 (impar)
        self.assertFalse(validar_cedula("1235"))

    def test_todos_ceros(self):
        self.assertTrue(validar_cedula("0000"))  # suma 0 (par)

if __name__ == "__main__":
    unittest.main()
