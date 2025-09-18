class Veiculo:
    def __init__(self, marca, modelo, ano):
        self._marca = marca
        self._modelo = modelo
        self._ano = ano

    def exibir_informacoes(self):
        return f'marca {self._marca}, modelo {self._modelo}, ano: {self._ano}'
    
    def ligar(self):
        return f'modelo {self._modelo} esta ligado'
    def desligar(self):

        return f'modelo {self._modelo} esta desligado'
