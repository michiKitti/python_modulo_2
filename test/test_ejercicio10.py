import unittest
from ejercicio10 import transponer_matriz, transponer_matriz_refactor

class TestTransponerMatriz(unittest.TestCase):
    def test_matriz_rectangular(self):
        m = [[1, 2, 3], [4, 5, 6]]
        esperado = [[1, 4], [2, 5], [3, 6]]
        self.assertEqual(transponer_matriz(m), esperado)
        self.assertEqual(transponer_matriz_refactor(m), esperado)

    def test_matriz_cuadrada(self):
        m = [[1, 2], [3, 4]]
        esperado = [[1, 3], [2, 4]]
        self.assertEqual(transponer_matriz(m), esperado)
        self.assertEqual(transponer_matriz_refactor(m), esperado)

    def test_matriz_un_elemento(self):
        m = [[7]]
        esperado = [[7]]
        self.assertEqual(transponer_matriz(m), esperado)
        self.assertEqual(transponer_matriz_refactor(m), esperado)

if __name__ == "__main__":
    unittest.main()
