from lista01.e03 import soma

def test_soma_0_0():
    assert soma(0, 0) == 0, "deve ser 0"

def test_soma_0_2():
    assert soma(0, 2) == 2, "deve ser 2"

def test_soma_2_2():
    assert soma(2, 2) == 4, "deve ser 4"

def test_soma_5_2():
    assert soma(5, 2) == 7, "deve ser 7"

def test_soma_100_2():
    assert soma(100, 2) == 102, "deve ser 102"

