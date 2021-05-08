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
            nome = dados['nome_completo']
            try:
                idade = int(dados['Idade'])
                cpf = int(dados['CPF'])
            except ValueError:
                self.__view.dado_invalido()
            else:
                novo_paciente = Paciente(nome, idade, cpf)
                lista_pacientes = list(self.__pacienteDAO.get_all())
                for paciente in lista_pacientes:
                    if paciente.cpf == cpf:
                        self.__view.paciente_duplicado()
                        return
                self.__pacienteDAO.add(novo_paciente)
                self.__view.cadastro_sucesso()


    def listagem(self):
        self.__view.listagem(list(self.__pacienteDAO.get_all()))


    def get_pacient_att(self):
        lista_pacientes = list(self.__pacienteDAO.get_all())
        return self.__view.get_pacient_att(lista_pacientes)


    def atualizar(self):
        paciente_escolhido = self.get_pacient_att()
        paciente_escolhido = paciente_escolhido[0].split('---')
        print(paciente_escolhido)
        try:
            idade_int = int(paciente_escolhido[1])
            cpf_int = int(paciente_escolhido[2])
        except ValueError:
            self.__view.dado_invalido()
        else:
            dados = self.__view.atualizar()
            lista_pacientes = list(self.__pacienteDAO.get_all())
            for paciente in lista_pacientes:
                if paciente.cpf == cpf_int:
                    paciente.nome_completo = dados[0]
                    paciente.idade = dados[1]


    def excluir(self):
        lista_pacientes = list(self.__pacienteDAO.get_all())
        pacientes_a_excluir = self.__view.excluir(lista_pacientes)
        if lista_pacientes != None and pacientes_a_excluir != None:
            for paciente in lista_pacientes:
                for exc in pacientes_a_excluir:
                        if paciente.nome_completo in exc and str(paciente.cpf) in exc:
                            self.__pacienteDAO.remove(paciente.cpf)
                            self.__view.sucesso_excluir()

    @property
    def pacientes(self):
        return list(self.__pacienteDAO.get_all())
