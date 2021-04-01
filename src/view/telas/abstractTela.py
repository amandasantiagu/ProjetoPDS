from abc import ABC, abstractmethod

class AbstractTela(ABC):

    def clear(self):
        lambda: os.system('cls' if os.name=='nt' else 'clear')


    def le_inteiro(msg: str = "", opcoes = []):
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
    def listar(self):
        pass


    @abstractmethod
    def atualizar(self):
        pass


    @abstractmethod
    def excluir(self):
        pass


