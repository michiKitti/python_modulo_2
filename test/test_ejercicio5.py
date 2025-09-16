import unittest
from ejercicio5 import validar_clasificador_de_numeros

class TestClasificadorNumeros(unittest.TestCase):
    def test_par(self):
        self.assertEqual(validar_clasificador_de_numeros(4), "El número 4 es Par.")

    def test_impar(self):
        self.assertEqual(validar_clasificador_de_numeros(7), "El número 7 es Impar.")

    def test_multiplo_de_5(self):
        self.assertEqual(
           validar_clasificador_de_numeros(10),
            "El número 10 es Par. Además, el número es múltiplo de 5."
        )

if __name__ == "__main__":
    unittest.main()
