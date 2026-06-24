def eh_par(numero):
    return numero % 2 == 0

def test_numero_par():
    assert eh_par(4) == True

def test_numero_impar():
    assert eh_par(3) == False

test_numero_par()
test_numero_impar() 