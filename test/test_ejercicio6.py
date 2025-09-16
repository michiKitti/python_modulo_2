import unittest

from ejercicio6 import validar_indice_letras


class TestValidarIndiceLetras(unittest.TestCase):

    def test_varias_ocurrencias(self):
        # "a" aparece en las posiciones 1,3,5
        self.assertEqual(validar_indice_letras("banana", "a"), [1, 3, 5])

    def test_una_ocurrencia(self):
        # "H" aparece en la posición 0
        self.assertEqual(validar_indice_letras("Hola", "H"), [0])

    def test_sin_ocurrencias(self):
        # "z" no aparece
        self.assertEqual(validar_indice_letras("perro", "z"), [])

    def test_mayusculas_minusculas(self):
        # busca "s" en varias mayúsculas/minúsculas
        self.assertEqual(validar_indice_letras("SENA sena SeNa", "s"), [0, 5, 10])



if __name__ == "__main__":
    unittest.main()
