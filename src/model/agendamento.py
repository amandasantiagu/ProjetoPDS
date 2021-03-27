from posto import PostoDeSaude

class Agendamento():
    def __init__(self, data: str, horario: str, posto: PostoDeSaude):
        self.__data = data
        self.__horario = horario
        self.__posto = posto

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
    def posto(self):
        return self.__posto

    @posto.setter
    def posto(self, posto):
        self.__posto = posto
