from ..model.paciente import Paciente
from ..view.tela_paciente import PacienteView
from ..view.tela_endereco import EnderecoView


class PacienteController():
    def __init__(self):
        self.__pacientes = [Paciente('Thais Helena', 70, 55124125112), Paciente('Lucas', 60, 10624125112)]
        self.__view = PacienteView()
        self.__endereco_view = EnderecoView()

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
        ##endereco = self.__endereco_view.novo()
        novo_paciente = Paciente(nome, idade, cpf)
        ##paciente.endereco = endereco
        for paciente in self.__pacientes:
            if paciente.cpf == cpf:
                self.__view.paciente_duplicado()
                return
        self.__pacientes.append(novo_paciente)
        self.__view.cadastro_sucesso()

    def listagem(self):
        self.__view.listagem(self.pacientes) 

    def atualizar(self):
        self.listagem()
        dados = self.__view.atualizar()
        for paciente in self.pacientes:
            if paciente.cpf == dados['cpf']:
                paciente.nome_completo = dados['nome_completo']
                paciente.idade = dados['idade']

    def excluir(self):
        self.listagem()
        cpf = self.__view.excluir()
        for paciente in self.pacientes:
            if paciente.cpf == cpf:
                self.__pacientes.remove(paciente)
                self.__view.sucesso_excluir()

    @property
    def pacientes(self):
        return self.__pacientes
