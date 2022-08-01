from lista01.e04 import notas

def test_media_0():
    assert notas(0, 0, 0, 0) == 0, "deve ser 0"

def test_media_1():
    assert notas(0, 0, 0, 4) == 1, "deve ser 1"

def test_soma_2_2():
    assert notas(0, 0, 4, 8) == 3, "deve ser 3"


