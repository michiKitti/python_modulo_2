

from ejercicio1 import validar_edad, validar_estudiante


def test_validar_edad():
    assert validar_edad(20) == 20000
    assert validar_edad(11) == 10000
    assert validar_edad(16) == 15000
