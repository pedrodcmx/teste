class locadora:
    def __init__(self):
        self.carros = []
        
    def adicionar_carro(self, modelo): 
        if not modelo:
            raise ValueError("Modelo indisponível")
        self.carros.append(modelo)
        
    def alugar_carro(self, modelo):
        if modelo not in self.carros:
            raise ValueError("O carro não está disponível")
        self.carros.remove(modelo)
        
    def quantidade_carros(self):
        return len(self.carros)