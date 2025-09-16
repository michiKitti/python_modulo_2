import unittest
from ejercicio12 import simulador_dados

class TestSimuladorDados(unittest.TestCase):
    def test_numero_de_lanzamientos(self):
        """
        Comprobar que el total de lanzamientos coincide con n_lanzamientos.
        """
        resultado = simulador_dados(100)
        self.assertEqual(sum(resultado.values()), 100)

    def test_rangos_de_suma(self):
        """
        Comprobar que todas las sumas estén en el rango válido (2 a 12).
        """
        resultado = simulador_dados(200)
        for clave in resultado.keys():
            self.assertTrue(2 <= clave <= 12)

if __name__ == "__main__":
    unittest.main()
