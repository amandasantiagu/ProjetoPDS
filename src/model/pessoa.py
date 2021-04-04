from abc import ABC, abstractmethod

class Pessoa(ABC):

    def __init__(self, nome_completo, idade):
        self.__nome_completo = nome_completo
        self.__idade = idade

    @property
    def nome_completo(self):
        return self.__nome_completo

    @nome_completo.setter
    def nome_completo(self, nome_completo):
        self.__nome_completo = nome_completo

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade
