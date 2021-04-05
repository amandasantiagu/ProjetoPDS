from .pessoa import Pessoa

class Paciente(Pessoa):
    def __init__(self, nome_completo, idade, cpf):
        super().__init__(nome_completo, idade)
        self.__cpf = cpf

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf
