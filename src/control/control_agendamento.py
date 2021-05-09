from ..model.paciente import Paciente
from ..model.agendamento import Agendamento
from ..model.enfermeiro import Enfermeiro
from ..model.vacina import Vacina
from ..model.persistence.agendamentoDAO import AgendamentoDAO
from ..view.agendamento_view import AgendamentoView
from ..view.vacina_view import VacinaView
from ..view.paciente_view import PacienteView
from ..view.enfermeiro_view import EnfermeiroView


class AgendamentoController():
    def __init__(self, posto, pac_controller, enf_controller):
        self.__dao = AgendamentoDAO()
        self.__agendamento_view = AgendamentoView()
        self.__vacina_view = VacinaView()
        self.__paciente_view = PacienteView()
        self.__enfermeiro_view = EnfermeiroView()
        self.__posto = posto
        self.__enfermeiro_controller = enf_controller
        self.__paciente_controller = pac_controller

    def option(self):
        escolha = self.__agendamento_view.tela_agendamento()
        while escolha != 'Sair' and escolha != None:
            options = {
                    'Incluir Agendamento': self.incluir,
                    'Listar Agendamentos':self.listagem,
                    'Atualizar Agendamento': self.atualizar,
                    'Remover Agendamento':  self.excluir
                    }
            function = options[escolha]
            function()
            escolha = self.__view.tela_agendamento()

    def incluir(self) -> Agendamento:
        dados = self.__agendamento_view.incluir()
        data = dados['data']
        horario = dados['horario']
        paciente = self.__paciente_view.selecionar(self.__paciente_controller.pacientes)
        enfermeiro = self.__enfermeiro_view.selecionar(self.__enfermeiro_controller.enfermeiros)
        vacina = self.__vacina_view.incluir()
        agendamento = Agendamento(data, horario, vacina, vacina['dose'], self.__posto, enfermeiro, paciente)
        for ag in self.__dao.get_all():
            if ag.data == data and ag.paciente == paciente:
                self.__agendamento_view.agendamento_duplicado()
                return
        self.__dao.add(agendamento)
        self.__agendamento_view.cadastro_sucesso()

    def excluir(self):
        dados = self.__agendamento_view.excluir()
        for agendamento in self.__dao.get_all():
            if agendamento.data == dados['data'] and agendamento.horario == dados['horario']:
                self.__dao.remove(agendamento.id)
                return

    ########### EM DUVIDA DE COMO ACESSAR MEU PACIENTE/ENFERMEIRO P EDITAR
    def atualizar(self, agendamento):
        dados = self.__agendamento_view.atualizar(agendamento)
        self.__dao.update(agendamento, agendamento.id)

    def listagem(self):
        self.__agendamento_view.listagem(self.__dao.get_all())

    @property
    def agendamentos(self):
        return self.__dao.get_all()
