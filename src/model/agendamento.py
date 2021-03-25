class Agendamento():
    def __init__(self, data: str, horario: str):
        self.__data = data
        self.__horario = horario

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