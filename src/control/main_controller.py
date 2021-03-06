from .control_enfermeiro import  EnfermeiroController
from .control_paciente import PacienteController
from .control_vacina import VacinaController
from .control_agendamento import AgendamentoController
from .control_posto import PostoController
from .control_relatorio import RelatorioController
from ..view.main_view import TelaSistemaView


class MainController:

    def __init__(self):
        self.__controller_posto = PostoController()
        self.__view = TelaSistemaView(self.__controller_posto.posto)
        self.__controller_paciente = PacienteController()
        self.__controller_enfermeiro = EnfermeiroController()
        self.__controller_vacina = VacinaController()
        

    def run(self):
        escolha = 'x'
        while escolha != 'Sair' and escolha != None:
            opcoes = {
                    'Paciente': self.__controller_paciente.option,
                    'Enfermeiro': self.__controller_enfermeiro.option,
                    'Vacinas': self.__controller_vacina.option,
                    'Agendamentos': self.agendamento,
                    'Relatório Geral': self.relatorio,
                    'Alterar Nome do Posto': self.__controller_posto.incluir,
                    }
            escolha = self.__view.menu_principal()
            try:
                opcoes[escolha]()
            except KeyError:
                return
    
    def agendamento(self):
        controller_agendamentos = AgendamentoController(self.__controller_paciente, self.__controller_enfermeiro, self.__controller_vacina)
        controller_agendamentos.option()
     
    def relatorio(self):
        controller_agendamentos = AgendamentoController(self.__controller_paciente, self.__controller_enfermeiro, self.__controller_vacina)
        controller_agendamentos.relatorio()


