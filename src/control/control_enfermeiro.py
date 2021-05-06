from ..model.enfermeiro import Enfermeiro
from ..view.enfermeiro_view import EnfermeiroView
from ..view.endereco_view import EnderecoView
from ..model.persistence.enfermeiroDAO import EnfermeiroDAO


class EnfermeiroController():
    def __init__(self):
        self.__enfermeiroDAO = EnfermeiroDAO()
        self.__view = EnfermeiroView()
        ##self.__endereco_view = EnderecoView()

    def option(self):
        escolha = self.__view.tela_enfermeiro()
        while escolha != 'Sair' and escolha != None:
            options = {
                    'Cadastrar Enfermeiro': self.incluir,
                    'Listar Enfermeiros': self.listagem,
                    'Atualizar Enfermeiro': self.atualizar,
                    'Remover Enfermeiro': self.excluir,
                    }
            function = options[escolha]
            function()
            escolha = self.__view.tela_enfermeiro()

    def incluir(self) -> Enfermeiro:
        dados = self.__view.incluir()
        if dados != None:
            nome = dados['nome_completo']
            try:
                idade = int(dados['idade'])
                matricula_coren = int(dados['matricula_coren'])
            except TypeError:
                self.__view.dado_invalido('CPF ou idade')
            #endereco = self.__endereco_view.novo()
            novo_enfermeiro = Enfermeiro(nome, idade, matricula_coren)
            #novo_enfermeiro.endereco = endereco
            lista_enfermeiros = list(self.__enfermeiroDAO.get_all())
            for enfermeiro in lista_enfermeiros:
                if enfermeiro.matricula_coren == matricula_coren:
                    self.__view.enfermeiro_duplicado()
                    return
            if novo_enfermeiro.idade < 0 and novo_enfermeiro.idade >= 180:
                self.__view.dado_invalido('idade')
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
        matricula_coren = self.__view.excluir()
        lista_enfermeiros = list(self.__enfermeiroDAO.get_all())
        for enfermeiro in self.enfermeiros:
            if enfermeiro.matricula_coren == matricula_coren:
                self.__enfermeiroDAO.remove(enfermeiro.matricula_coren)
                self.__view.sucesso_excluir()

    @property
    def enfermeiros(self):
        return list(self.__enfermeiroDAO.get_all())
