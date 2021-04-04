import os
from abc import ABC, abstractmethod

class AbstractView(ABC):
    @abstractmethod
    def __init__(self):
        pass

    def clear(self):
        lambda: os.system('cls' if os.name=='nt' else 'clear')

    def le_inteiro(self, msg: str = "", opcoes = []):
        while True:
            value = input(msg)
            try:
                opcao = int(value)
                if opcao not in opcoes:
                    raise ValueError
                return opcao
            except ValueError:
                print('Valor inválido. Tente novamente.')
                if (len(opcoes) != 0):
                    print("Valores válidos: ", opcoes)

    @abstractmethod
    def incluir(self):
        pass

    @abstractmethod
    def excluir(self):
        pass

    @abstractmethod
    def listagem(self):
        pass

    @abstractmethod
    def atualizar(self):
        pass
