def test_validar_idade():
    try:
        assert validar_idade(18) == 'Maior de idade'
    except AssertionError:
        print ('Erro ao validar idade')

        
def validar_idade(idade):
    if idade >= 18:
        return 'Maior de idade'
    else:
        return 'Menor de idade'
    
test_validar_idade()