from ..model.paciente import Paciente
from ..view.paciente_view import PacienteView
from ..view.endereco_view import EnderecoView
from ..model.persistence.pacienteDAO import PacienteDAO


class PacienteController():
    def __init__(self):
        self.__pacienteDAO = PacienteDAO()
        self.__view = PacienteView()
        #self.__endereco_view = EnderecoView()

    def option(self):
        escolha = self.__view.tela_paciente()
        while escolha != 'Sair' and escolha != None:
            options = {
                    'Cadastrar Paciente': self.incluir,
                    'Listar Pacientes': self.listagem,
                    'Atualizar Paciente': self.atualizar,
                    'Remover Paciente': self.excluir,
                    }
            function = options[escolha]
            function()
            escolha = self.__view.tela_paciente()

    def incluir(self) -> Paciente:
        dados = self.__view.incluir()
        if dados != None:
            nome = dados[0]
            idade = dados[1]
            try:
                cpf = int(dados[2])
            except TypeError:
                self.__view.dado_invalido('cpf')
            # endereco = self.__endereco_view.novo()
            novo_paciente = Paciente(nome, idade, cpf)
            #novo_paciente.endereco = endereco
            lista_pacientes = list(self.__pacienteDAO.get_all())
            for paciente in lista_pacientes:
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
            if paciente.cpf == dados[0]:
                paciente.nome_completo = dados[1]
                paciente.idade = dados[2]


    def excluir(self):
        cpf = self.__view.excluir()
        lista_pacientes = list(self.__pacienteDAO.get_all())
        for paciente in lista_pacientes:
            if paciente.cpf == cpf:
                self.__pacienteDAO.remove(paciente.cpf)
                self.__view.sucesso_excluir()

    @property
    def pacientes(self):
        return list(self.__pacienteDAO.get_all())
