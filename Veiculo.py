class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano

    def exibir_informacoes(self):
        return f'marca {self.__marca}, modelo {self.__modelo}, ano: {self.__ano}'
    
    def ligar(self):
        return f'modelo {self.__modelo} esta ligado'
    def desligar(self):
        return f'modelo {self.__modelo} esta desligado'