from .pessoa import Pessoa
from .paciente import Paciente
from .persistence.agendamentoDAO import AgendamentoDAO

class Enfermeiro(Pessoa):

    def __init__(self, nome_completo, idade, matricula_coren):
        super().__init__(nome_completo, idade)
        self.__matricula_coren = matricula_coren
        

    @property
    def matricula_coren(self):
        return self.__matricula_coren

    @matricula_coren.setter
    def matricula_coren(self, matricula_coren):
        self.__matricula_coren = matricula_coren

    def pacientes(self):
        pacientes = []
        dao = AgendamentoDAO()
        for item in dao.get_all():
            if item.enfermeiro.matricula_coren == self.__matricula_coren:
                pacientes.append(item.paciente)


        return pacientes
