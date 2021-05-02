from ..model.paciente import Paciente
from ..view.tela_paciente import PacienteView
from ..view.tela_endereco import EnderecoView
from .abstractDAO import AbstractDAO


class PacienteController():
    def __init__(self):
        self.__pacienteDAO = PacienteDAO()
        self.__view = PacienteView()
        #self.__endereco_view = EnderecoView()

    def option(self):
        escolha = self.__view.tela_paciente()
        while escolha != 0:
            options = {
                    1: self.incluir,
                    2: self.excluir,
                    3: self.atualizar,
                    4: self.listagem,
                    }
            function = options[escolha]
            function()
            escolha = self.__view.tela_paciente()

    def incluir(self) -> Paciente:
        dados = self.__view.incluir()
        nome = dados['nome_completo']
        idade = dados['idade']
        cpf = dados['cpf']
        # endereco = self.__endereco_view.novo()
        novo_paciente = Paciente(nome, idade, cpf)
        #novo_paciente.endereco = endereco
        for paciente in self.__pacientes:
            if paciente.cpf == cpf:
                self.__view.paciente_duplicado()
                return
        self.__pacienteDAO.add(novo_paciente)
        self.__view.cadastro_sucesso()

    def listagem(self):
        self.__view.listagem(list(self.__pacienteDAO.get_all()))

    def atualizar(self):
        self.listagem()
        dados = self.__view.atualizar()
        lista_pacientes = list(self.__pacienteDAO.get_all())
        for paciente in lista_pacientes:
            if paciente.cpf == dados['cpf']:
                paciente.nome_completo = dados['nome_completo']
                paciente.idade = dados['idade']


    def excluir(self):
        self.listagem()
        cpf = self.__view.excluir()
        lista_pacientes = list(self.__pacienteDAO.get_all())
        for paciente in lista_pacientes:
            if paciente.cpf == cpf:
                self.__pacienteDAO.remove(paciente.cpf)
                self.__view.sucesso_excluir()

    @property
    def pacientes(self):
        return list(self.__pacienteDAO.get_all())
