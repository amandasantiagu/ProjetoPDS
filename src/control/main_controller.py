from control.control_enfermeiro import  EnfermeiroController
from control.control_paciente import PacienteController
from control.control_agendamento import AgendamentoController
from view.tela_sistema import TelaSistemaView

class MainController:

    def __init__(self):
        self.__view = TelaSistemaView()
        self.__controller_paciente = PacienteController()
        self.__controller_enfermeiro = EnfermeiroController()
        self.__controller_agendamentos = AgendamentoController(self.__controller_paciente, self.__controller_enfermeiro)
        opcoes = {
                1: self.__controller_paciente.incluir,
                2: self.__controller_enfermeiro.incluir,
                3: self.__controller_agendamentos.incluir,
                4: self.__controller_agendamentos.relatorio,
                0: self.sair,
                }
        escolha = self.__view.menu_principal()
        opcoes[escolha]() #isso roda o método que o usuário escolher

    def sair(self):
        return
