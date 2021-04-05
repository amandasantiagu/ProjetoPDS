from .control_enfermeiro import  EnfermeiroController
from .control_paciente import PacienteController
from .control_agendamento import AgendamentoController
from .control_posto import PostoController
from ..view.tela_sistema import TelaSistemaView

class MainController:

    def __init__(self):
        self.__posto = None

    def run(self):
        escolha = 'x'
        while escolha != 0:
            if self.primeiro_posto():
                self.__posto = PostoController().incluir()

            self.__view = TelaSistemaView()
            self.__controller_paciente = PacienteController()
            self.__controller_enfermeiro = EnfermeiroController()
            self.__controller_agendamentos = AgendamentoController(self.__posto, self.__controller_paciente, self.__controller_enfermeiro)
            opcoes = {
                    1: self.incluir_paciente,
                    2: self.__controller_enfermeiro.incluir,
                    3: self.__controller_agendamentos.incluir,
                    4: self.__controller_agendamentos.relatorio,
                    0: self.sair,
                    }
            escolha = self.__view.menu_principal()
            try:
                opcoes[escolha]() 
            except [ValueError, KeyError]:
                print('Opção inválida. Tente novamente.')
                continue

    
    def incluir_paciente(self):
        return self.__controller_paciente.incluir()


    def primeiro_posto(self):
        return self.__posto is None

    def sair(self):
        exit()
