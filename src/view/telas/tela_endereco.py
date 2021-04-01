from models.endereco import Endereco

class TelaEndereco:

    def novo(self):
        rua = input("Nome da Rua: ")
        num_casa = input("Número da Casa: ")
        cidade = input("Cidade: ")
        return Endereco(cidade, rua, num_casa)
