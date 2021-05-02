from ..model.enfermeiro import Enfermeiro
from ..view.tela_enfermeiro import EnfermeiroView
from ..view.tela_endereco import EnderecoView
from .abstractDAO import AbstractDAO


class EnfermeiroController():
    def __init__(self):
        self.__enfermeiroDAO = EnfermeiroDAO()
        self.__view = EnfermeiroView()
        ##self.__endereco_view = EnderecoView()

    def option(self):
        escolha = self.__view.tela_enfermeiro()
        while escolha != 0:
            options = {
                    1: self.incluir,
                    2: self.excluir,
                    3: self.atualizar,
                    4: self.listagem,
                    }
            function = options[escolha]
            function()
            escolha = self.__view.tela_enfermeiro()

    def incluir(self) -> Enfermeiro:
        dados = self.__view.incluir()
        nome = dados['nome_completo']
        idade = dados['idade']
        matricula_coren = dados['matricula_coren']
        #endereco = self.__endereco_view.novo()
        novo_enfermeiro = Enfermeiro(nome, idade, matricula_coren)
        novo_enfermeiro.endereco = endereco
        for enfermeiro in self.__enfermeiros:
            if enfermeiro.matricula_coren == matricula_coren:
                self.__view.enfermeiro_duplicado()
                return
        if novo_enfermeiro.idade < 0 and novo_enfermeiro.idade >= 180:
            self.__view.dado_invalido("Idade")
            print("Idade")
            return 

        self.__enfermeiroDAO.add(novo_enfermeiro)
        self.__view.cadastro_sucesso()

    def listagem(self):
        self.__view.listagem(list(self.__enfermeiroDAO.get_all()))

    def atualizar(self):
        self.listagem()
        dados = self.__view.atualizar()
        lista_enfermeiros = list(self.__enfermeiroDAO.get_all())
        for enf in lista_enfermeiros:
            if enf.matricula_coren == dados['matricula_coren']:
                enf.nome_completo = dados['nome_completo']
                enf.idade = dados['idade']
                self.__view.sucesso_atualizar()

    def excluir(self):
        self.listagem()
        matricula_coren = self.__view.excluir()
         lista_enfermeiros = list(self.__enfermeiroDAO.get_all())
        for enfermeiro in self.enfermeiros:
            if enfermeiro.matricula_coren == matricula_coren:
                self.__enfermeiroDAO.remove(enfermeiro.matricula_coren)
                self.__view.sucesso_excluir()

    @property
    def enfermeiros(self):
        return list(self.__enfermeiroDAO.get_all())
