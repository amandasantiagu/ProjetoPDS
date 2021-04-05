from .control_enfermeiro import  EnfermeiroController
from .control_paciente import PacienteController
from .control_agendamento import AgendamentoController
from .control_posto import PostoController
from .control_relatorio import RelatorioController
from ..view.tela_sistema import TelaSistemaView

class MainController:

    def __init__(self):
        self.__posto = None
        self.__view = TelaSistemaView()
        self.__controller_paciente = PacienteController()
        self.__controller_enfermeiro = EnfermeiroController()
        self.__controller_agendamentos = AgendamentoController(self.__posto, self.__controller_paciente, self.__controller_enfermeiro)
        self.__controller_relatorio = RelatorioController(self.__controller_paciente, self.__controller_agendamentos)

    def run(self):
        escolha = 'x'
        while escolha != 0:
            if self.primeiro_posto():
                self.__posto = PostoController().incluir()

            opcoes = {
                    1: self.__controller_paciente.option,
                    2: self.__controller_enfermeiro.option,
                    3: self.__controller_agendamentos.option,
                    4: self.__controller_relatorio.relatorio,
                    0: self.sair
                    }
            escolha = self.__view.menu_principal()
            try:
                opcoes[escolha]() 
            except KeyError:
                print('Opção inválida. Tente novamente.')
                continue

    
    def primeiro_posto(self):
        return self.__posto is None
    
    def sair(self):
        exit()


