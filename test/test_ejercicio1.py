

from ejercicio1 import validar_edad, validar_estudiante

def test_validar_estudiante():
    assert validar_estudiante("si",20000)== 18000
    assert validar_estudiante("no",20000)== 20000