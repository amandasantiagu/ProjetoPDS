from model.paciente import Paciente
from model.agendamento import Agendamento
from model.enfermeiro import Enfermeiro
from model.vacina import Vacina
from view.telas.tela_agendamento import AgendamentoView
from view.telas.tela_vacina import VacinaView
from view.telas.tela_paciente import PacienteView
from view.telas.tela_enfermeiro import EnfermeiroView


class AgendamentoController():
    def __init__(self, enf_controller, pac_controller):
        self.__agendamentos = []
        self.__agendamento_view = AgendamentoView()
        self.__vacina_view = VacinaView()
        self.__paciente_view = PacienteView()
        self.__enfermeiro_view = EnfermeiroView()
        self.__enfermeiro_controller = enf_controller
        self.__paciente_controller = pac_controller



    def option(self):
        escolha = self.__view.tela_agendamento()
        options = {
                1: incluir,
                2: excluir,
                3: atualiza,
                4: listagem,
                0: self.clear,
                }


    def incluir(self) -> Agendamento:
        dados = self.__view.incluir()
        data = dados['data']
        horario = dados['horario']
        paciente = self.__enfermeiro_view.selecionar(self.enf_controller.pacientes)
        enfermeiro = self.__enfermeiro_view.selecionar(self.__enfermeiro_controller.enfermeiros)
        vacina = self.__vacina_view.incluir()
        agendamento = Agendamento(data, horario, posto, vacina, enfermeiro, paciente)
        for ag in self.__agendamentos:
            if ag.data == data and ag.paciente == paciente:
                self.__view.agendamento_duplicado()
                return
        if agendamento.idade < 0:
            self.__view.dado_invalido("Idade")
        self.__agendamentos.append(agendamento)
        self.__view.cadastro_sucesso()

    def listagem(self):
        self.__view.listagem(self.agendamentos) 


    def excluir(self):
        dados = self.__view.excluir()
        for agendamento in self.__agendamentos:
            if agendamento.data == dados['data'] and agendamento.horario == dados['horario']:
                self.__agendamentos.remove(agendamento)
                return


