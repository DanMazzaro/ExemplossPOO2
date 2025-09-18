from Veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, portas):
        super().__init__(marca, modelo, ano)
        self._portas = portas

    def abrir_porta(self):
        return f'a porta do {self._modelo} foi aberta'

    def exibir_informacoes(self):
        info_veiculo = super().exibir_informacoes()

        return f'{info_veiculo}, portas {self._portas}'
