from model.paciente import Paciente
from view.telas.tela_paciente import PacienteView
from view.telas.tela_endereco import EnderecoView


class PacienteController():
    def __init__(self):
        self.__pacientes = []
        self.__view = PacienteView()


    def option(self):
        escolha = self.__view.tela_paciente()
        options = {
                1: incluir,
                2: excluir,
                3: atualiza,
                4: listagem,
                0: self.clear,
                }


    def incluir(self) -> Paciente:
        dados = self.__view.incluir()
        nome = dados['nome_completo']
        cpf = dados['cpf']
        idade = dados['idade']
        endereco = TelaEndereco().novo()
        paciente = Paciente(nome, cpf, idade)
        paciente.endereco = endereco
        for paciente in self.__pacientes:
            if paciente.cpf == cpf:
                self.__view.paciente_duplicado()
                return
        if paciente.idade < 0:
            self.__view.dado_invalido("Idade")
        self.__pacientes.append(paciente)
        self.__view.cadastro_sucesso()

    def listagem(self):
        self.__view.listagem(self.pacientes) 

    def atualiza(self):
        dados = self.__view.atualiza()
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


