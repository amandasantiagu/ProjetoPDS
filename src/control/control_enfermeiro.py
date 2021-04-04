from model.enfermeiro import Enfermeiro
from view.tela_enfermeiro import EnfermeiroView
from view.tela_endereco import EnderecoView


class EnfermeiroController():
    def __init__(self):
        self.__enfermeiros = []
        self.__view = EnfermeiroView()
        self.__endereco_view = EnderecoView()

    def option(self):
        escolha = self.__view.tela_enfermeiro()
        options = {
                1: self.incluir,
                2: self.excluir,
                3: self.atualizar,
                4: self.listagem,
                0: self.sair,
                }
        function = options[escolha]
        function()

    def incluir(self) -> Enfermeiro:
        dados = self.__view.incluir()
        nome = dados['nome_completo']
        idade = dados['idade']
        matricula_coren = dados['matricula_coren']
        endereco = self.__endereco_view.novo()
        enfermeiro = Enfermeiro(nome, idade, matricula_coren)
        enfermeiro.endereco = endereco
        for enfermeiro in self.__enfermeiros:
            if enfermeiro.matricula_coren == matricula_coren:
                self.__view.enfermeiro_duplicado()
                return
        if enfermeiro.idade < 0 and enfermeiro.idade >= 180:
            self.__view.dado_invalido("Idade")
        self.__enfermeiros.append(enfermeiro)
        self.__view.cadastro_sucesso()

    def listagem(self):
        self.__view.listagem(self.enfermeiros) 

    def atualizar(self):
        dados = self.__view.atualizar()
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

    def sair(self):
        return

    @property
    def enfermeiros(self):
        return self.__enfermeiros
