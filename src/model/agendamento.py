from .paciente import Paciente
from .enfermeiro import Enfermeiro
from .vacina import Vacina
from .posto import Posto

class Agendamento():
    def __init__(self, data: str,
                 horario: str,
                 vacina: Vacina,
                 posto: Posto,
                 enfermeiro: Enfermeiro = None,
                 paciente: Paciente = None):
        self.__data = data
        self.__horario = horario
        self.__vacina = vacina
        self.__posto = posto
        self.__enfermeiro = enfermeiro
        self.__paciente = paciente

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def horario(self):
        return self.__horario

    @horario.setter
    def horario(self, horario):
        self.__horario = horario

    @property
    def enfermeiro(self):
        return self.__enfermeiro

    @enfermeiro.setter
    def enfermeiro(self, enfermeiro):
        self.__enfermeiro = enfermeiro

    @property
    def paciente(self):
        return self.__paciente

    @paciente.setter
    def paciente(self, paciente):
        self.__paciente = paciente


    @property
    def vacina(self):
        return self.__vacina

    @vacina.setter
    def vacina(self, vacina):
        self.__vacina = vacina


