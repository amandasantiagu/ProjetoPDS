from abstractDAO import AbstractDAO

class AgendamentoDAO(AbstractDAO):
    def __init__(self):
        super().__init__('agendamentos.pkl')


    def add(self, agendamento):
        super().add(agendamento)



    def get(self, key):
        return super().get(key)


    def remove(self, key):
        return super().remove(key)


    def get_all(self):
        return super()get_all()
