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
            nome = dados[0]
            try:
                idade = int(dados[1])
                matricula_coren = int(dados[2])
            except ValueError:
                self.__view.dado_invalido('Idade e Matricula sao inteiros')
            else:
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

    def get_enfermeiro_att(self):
        lista_enfermeiros = list(self.__enfermeiroDAO.get_all())
        return self.__view.get_enfermeiro_att(lista_enfermeiros)


    def atualizar(self):
        enfermeiro_escolhido = self.get_enfermeiro_att()
        enfermeiro_escolhido = enfermeiro_escolhido[0].split('---')
        try:
            idade_int = int(enfermeiro_escolhido[1])
            matricula_coren_int = int(enfermeiro_escolhido[2])
        except ValueError:
            self.__view.dado_invalido()
        else:
            dados = self.__view.atualizar()
            lista_enfermeiros = list(self.__enfermeiroDAO.get_all())
            for enfermeiro in lista_enfermeiros:
                if enfermeiro.matricula_coren == matricula_coren_int:
                    enfermeiro.nome_completo = dados[0]
                    enfermeiro.idade = dados[1]

    def excluir(self):
        lista_enfermeiros = list(self.__enfermeiroDAO.get_all())
        enfermeiros_a_excluir = self.__view.selecionar(lista_enfermeiros, acao='Excluir')
        if lista_enfermeiros != None and enfermeiros_a_excluir != None:
            for enfermeiros in lista_enfermeiros:
                for exc in enfermeiros_a_excluir:
                        if enfermeiro.nome_completo in exc and str(enfermeiro.matricula_coren) in exc:
                            self.__enfermeiroDAO.remove(enfermeiro.matricula_coren)
                            self.__view.sucesso_excluir()

    @property
    def enfermeiros(self):
        return list(self.__enfermeiroDAO.get_all())
