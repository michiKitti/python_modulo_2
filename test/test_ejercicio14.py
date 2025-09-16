import unittest
from io import StringIO
from contextlib import redirect_stdout

from ejercicio_ahorcado import mostrar_tablero, validar_entrada, jugar_ahorcado


class TestAhorcado(unittest.TestCase):

    def test_mostrar_tablero_vacio(self):
        s = mostrar_tablero("hola", set(), 6)
        self.assertIn("Palabra:", s)
        self.assertIn("_ _ _ _", s)  # cuatro guiones (espaciados)
        self.assertIn("Vidas restantes: 6", s)

    def test_mostrar_tablero_parcial(self):
        s = mostrar_tablero("hola", {"h", "a"}, 5)
        # debe mostrar h y a, otros guiones
        self.assertIn("h _ _ a", s.replace("Palabra:  ", ""))  # quitamos prefijo para verificar

    def test_validar_entrada_invalida(self):
        valido, msg = validar_entrada("", set())
        self.assertFalse(valido)
        self.assertTrue("Ingresa solo una letra" in msg)

        valido, msg = validar_entrada("aa", set())
        self.assertFalse(valido)

        valido, msg = validar_entrada("1", set())
        self.assertFalse(valido)

    def test_validar_entrada_repetida(self):
        valido, msg = validar_entrada("a", {"a"})
        self.assertFalse(valido)
        self.assertIn("Ya intentaste", msg)

    def test_juego_ganar(self):
        # palabra: "oro" -> letras objetivo o,r
        comandos = ["o", "r"]
        buf = StringIO()
        with redirect_stdout(buf):
            resultado, palabra = jugar_ahorcado(palabra_secreta="oro", comandos=comandos)
        salida = buf.getvalue()
        self.assertEqual(resultado, "ganaste")
        self.assertIn("¡Ganaste!", salida)

    def test_juego_perder(self):
        # intentos errados suficientes para perder con 6 vidas
        comandos = list("bcdfgh")  # suposiciones erradas
        buf = StringIO()
        with redirect_stdout(buf):
            resultado, palabra = jugar_ahorcado(palabra_secreta="zz", comandos=comandos)
        salida = buf.getvalue()
        self.assertEqual(resultado, "perdiste")
        self.assertIn("Perdiste", salida)


if __name__ == "__main__":
    unittest.main()
