import unittest
from ejercicio4 import determinar_ganador, jugar_ronda


class TestJuegoPiedraPapelTijeras(unittest.TestCase):

    def test_empate(self):
        # Si ambos eligen lo mismo → empate
        self.assertEqual(determinar_ganador("piedra", "piedra"), "empate")
        self.assertEqual(determinar_ganador("papel", "papel"), "empate")
        self.assertEqual(determinar_ganador("tijeras", "tijeras"), "empate")

    def test_gana_jugador(self):
        # Casos donde el jugador gana
        self.assertEqual(determinar_ganador("piedra", "tijeras"), "jugador")
        self.assertEqual(determinar_ganador("tijeras", "papel"), "jugador")
        self.assertEqual(determinar_ganador("papel", "piedra"), "jugador")

    def test_gana_pc(self):
        # Casos donde la PC gana
        self.assertEqual(determinar_ganador("tijeras", "piedra"), "pc")
        self.assertEqual(determinar_ganador("papel", "tijeras"), "pc")
        self.assertEqual(determinar_ganador("piedra", "papel"), "pc")

    def test_option_invalida(self):
        # Si el jugador escribe algo que no es válido

            ganador, mensaje = jugar_ronda("lagarto", "piedra")
            self.assertEqual(ganador, "Opción no válida.")
            self.assertEqual(ganador, "Opción no válida.")


if __name__ == "__main__":
    unittest.main()

