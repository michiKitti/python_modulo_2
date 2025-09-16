import unittest
from ejercicio9 import filtrado_datos

class TestFiltradoDatos(unittest.TestCase):

    def test_listas_generadas(self):
        resultado = filtrado_datos()
        self.assertEqual(resultado["positivos"], [10, 20, 30])
        self.assertEqual(
            resultado["cuadrados"],
            [25, 100, 225, 400, 625, 900]
        )
        self.assertEqual(
            resultado["etiquetas"],
            ["negativo", "positivo", "negativo", "positivo", "negativo", "positivo"]
        )

if __name__ == "__main__":
    unittest.main()
