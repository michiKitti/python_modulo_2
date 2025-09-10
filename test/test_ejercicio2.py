import unittest
from ejercicio2 import interprete_comandos

class TestValidarComandos(unittest.TestCase):

    def test_validar_comandos(self):
        self.assertTrue(interprete_comandos("guardar"))
        self.assertTrue(interprete_comandos("cargar"))
        self.assertTrue(interprete_comandos("salir"))
        self.assertFalse(interprete_comandos("comando invalido"))

