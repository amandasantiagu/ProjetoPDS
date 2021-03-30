from pessoa import Pessoa

class Paciente():
    def __init__(self, nome: str, sobrenome: str, cpf: int, idade: int):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__idade = idade
        
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def sobrenome(self):
        return self.__sobrenome

    @sobrenome.setter
    def sobrenome(self, sobrenome):
        self.__sobrenome = sobrenome

    @property
    def cpf(self):
        return self.__cpf
        
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf
        
    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade
