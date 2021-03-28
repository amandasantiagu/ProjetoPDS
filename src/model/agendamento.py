class Agendamento():
    def __init__(self, data: str, horario: str, dosagem_vacina: int):
        self.__data = data
        self.__horario = horario
        self.__dosagem_vacina = dosagem_vacina

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