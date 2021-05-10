from .paciente import Paciente
from .enfermeiro import Enfermeiro
from .vacina import Vacina

class Agendamento():
    def __init__(self, 
                 num_id: int,
                 data: str,
                 horario: str,
                 vacina: Vacina,
                 dose_vacina: int,
                 enfermeiro: Enfermeiro = None,
                 paciente: Paciente = None):
        self.__num_id = num_id
        self.__data = data
        self.__horario = horario
        self.__vacina = vacina
        self.__dose_vacina = dose_vacina
        self.__enfermeiro = enfermeiro
        self.__paciente = paciente


    @property
    def num_id(self):
        return self.__num_id


    @num_id.setter
    def num_id(self, num_id):
        self.__num_id = num_id


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


    @property
    def dose_vacina(self):
        return self.__dose_vacina

    @dose_vacina.setter
    def dose_vacina(self, dose_vacina):
        self.__dose_vacina = dose_vacina


