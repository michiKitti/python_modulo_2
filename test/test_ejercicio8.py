import unittest
from ejercicio8 import filtrado_datos


class TestFiltradoDatos(unittest.TestCase):
    def test_resultados(self):
        positivos, cuadrados, etiquetas = filtrado_datos()

        self.assertEqual(positivos, [10, 20, 30])
        self.assertEqual(cuadrados, [25, 100, 225, 400, 625, 900])
        self.assertEqual(
            etiquetas,
            ["negativo", "positivo", "negativo", "positivo", "negativo", "positivo"]
        )

if __name__ == "__main__":
    unittest.main()
