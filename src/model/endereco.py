from abc import ABC, abstractmethod


class Endereco(ABC):
    @abstractmethod  
    def __init__(self,  cidade: str, rua: str, num_casa: int):
        self.__rua = rua
        self.__num_casa = num_casa
        self.__cidade = cidade

    @property
    def cidade(self):
        return self.__cidade
        
    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade

    @property
    def rua(self):
        return self.__rua
        
    @rua.setter
    def rua(self, rua):
        self.__rua = rua

    @property
    def num_casa(self):
        return self.__num_casa

    @num_casa.setter
    def num_casa(self, num_casa):
        self.__num_casa = num_casa