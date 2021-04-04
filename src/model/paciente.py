
from model.pessoa import Pessoa

class Paciente(Pessoa):
    def __init__(self, nome_completo, idade, cpf):
        self.__cpf = cpf
        super().__init__(nome_completo, idade)