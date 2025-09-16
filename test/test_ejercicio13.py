import unittest
from ejercicio13 import aventura_texto

class TestAventuraTexto(unittest.TestCase):
    def test_camino_ganar(self):
        comandos = ["ir al norte", "abrir cofre", "luchar"]
        resultado = aventura_texto(comandos)
        self.assertEqual(resultado, "ganaste")

    def test_camino_perder(self):
        comandos = ["ir al norte", "abrir cofre", "huir"]
        resultado = aventura_texto(comandos)
        self.assertEqual(resultado, "perdiste")

if __name__ == "__main__":
    unittest.main()
