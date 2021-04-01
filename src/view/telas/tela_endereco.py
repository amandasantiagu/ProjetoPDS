from models.endereco import Endereco
from abstractView import abstractView

class EnderecoView(AbstractView):

    def novo(self):
        rua = input("Nome da Rua: ")
        num_casa = input("Número da Casa: ")
        cidade = input("Cidade: ")
        return Endereco(cidade, rua, num_casa)
