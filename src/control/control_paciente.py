from ..model.paciente import Paciente
from ..view.tela_paciente import PacienteView
from ..view.tela_endereco import EnderecoView


class PacienteController():
    def __init__(self):
        self.__pacientes = []
        self.__view = PacienteView()
        self.__endereco_view = EnderecoView()

    def option(self):
        escolha = self.__view.tela_paciente()
        options = {
                1: self.incluir,
                2: self.excluir,
                3: self.atualizar,
                4: self.listagem,
                0: self.sair,
                }
        function = options[escolha]
        function()

    def incluir(self) -> Paciente:
        dados = self.__view.incluir()
        nome = dados['nome_completo']
        cpf = dados['cpf']
        idade = dados['idade']
        endereco = self.__endereco_view.novo()
        paciente = Paciente(nome, cpf, idade)
        paciente.endereco = endereco
        for paciente in self.__pacientes:
            if paciente.cpf == cpf:
                self.__view.paciente_duplicado()
                return
        self.__pacientes.append(paciente)
        self.__view.cadastro_sucesso()

    def listagem(self):
        self.__view.listagem(self.pacientes) 

    def atualizar(self):
        dados = self.__view.atualizar()
        for paciente in self.pacientes:
            if paciente.cpf == dados['cpf']:
                paciente.nome_completo = dados['nome_completo']
                paciente.idade = dados['idade']

    def excluir(self):
        cpf = self.__view.excluir()
        for paciente in self.pacientes:
            if paciente.cpf == cpf:
                self.__pacientes.remove(paciente)
                return

    @property
    def pacientes(self):
        return self.__pacientes
