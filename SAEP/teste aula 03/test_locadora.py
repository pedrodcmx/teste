from locadora import locadora

def test_adicionar_carro():
    lc = locadora()
    lc.adicionar_carro("Chevrolet Astra")
    assert lc.quantidade_carros() == 1
    
def test_alugar_carro()
    lc = locadora()
    lc.adicionar_carro("O Volkswagen Polo")
    lc.alugar_carro("O Volkswagen Polo")
    assert lc.quantidade_carros() == 0
    
test_adicionar_carro()
test_alugar_carro()