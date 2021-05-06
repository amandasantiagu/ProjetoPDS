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
        self.__controller_agendamentos = AgendamentoController(self.__controller_posto.posto, self.__controller_paciente, self.__controller_enfermeiro)
        self.__controller_relatorio = RelatorioController(self.__controller_paciente, self.__controller_agendamentos)
        

    def run(self):
        escolha = 'x'
        while escolha != 'Sair' and escolha != None:
            opcoes = {
                    'Cadastrar Paciente': self.__controller_paciente.option,
                    'Cadastro do Enfermeiro': self.__controller_enfermeiro.option,
                    'Cadastro de Vacinas': self.__controller_vacina.option,
                    'Agendamentos': self.__controller_agendamentos.option,
                    'Gerar Relatório Geral': self.__controller_relatorio.relatorio,
                    'Alterar nome do Posto': self.__controller_posto.incluir,
                    }
            escolha = self.__view.menu_principal()
            opcoes[escolha]()
    
    def sair(self):
        return


