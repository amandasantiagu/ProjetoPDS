from model.enfermeiro import Enfermeiro
from view.telas.tela_enfermeiro import EnfermeiroView
from view.telas.tela_endereco import TelaEndereco


class EnfermeiroController():
    def __init__(self):
        self.__enfermeiros = []
        self.__view = EnfermeiroView()


    def option(self):
        escolha = self.__view.tela_enfermeiro()
        options = {
                1: incluir,
                2: excluir,
                3: atualiza,
                4: listagem,
                0: self.clear,
                }


    def incluir(self) -> Enfermeiro:
        dados = self.__view.incluir()
        nome = dados['nome_completo']
        cpf = dados['cpf']
        idade = dados['idade']
        endereco = TelaEndereco().novo()
        enfermeiro = Enfermeiro(nome, cpf, idade)
        enfermeiro.endereco = endereco
        for enfermeiro in self.__enfermeiros:
            if enfermeiro.cpf == cpf:
                self.__view.enfermeiro_duplicado()
                return
        if enfermeiro.idade < 0:
            self.__view.dado_invalido("Idade")
        self.__enfermeiros.append(enfermeiro)
        self.__view.cadastro_sucesso()

    def listagem(self):
        self.__view.listagem(self.enfermeiros) 

    def atualiza(self):
        dados = self.__view.atualiza()
        for enfermeiro in self.enfermeiros:
            if enfermeiro.cpf == dados['cpf']:
                enfermeiro.nome_completo = dados['nome_completo']
                enfermeiro.idade = dados['idade']

    def excluir(self):
        cpf = self.__view.excluir()
        for enfermeiro in self.enfermeiros:
            if enfermeiro.cpf == cpf:
                self.__enfermeiros.remove(enfermeiro)
                return


