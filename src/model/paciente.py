class Paciente():
    def __init__(self, nome_completo: str, cpf: int, idade: int):
        self.__nome_completo = nome_completo
        self.__cpf = cpf
        self.__idade = idade
        
    @property
    def nome_completo(self):
        return self.__nome_completo

    @nome_completo.setter
    def nome_completo(self, nome_completo):
        self.__nome_completo = nome_completo

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