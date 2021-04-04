
from model.endereco import Endereco

class EnderecoView():

    def __init__(self):
        pass

    def novo(self):
        rua = input("Nome da Rua: ")
        num_casa = input("Número da Casa: ")
        cidade = input("Cidade: ")
        return Endereco(cidade, rua, num_casa)
