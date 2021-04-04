from model.pessoa import Pessoa
class Enfermeiro(Pessoa):

    def __init__(self, nome_completo, idade, matricula_coren):
        super().__init__(nome_completo, idade)
        self.__matricula_coren = matricula_coren
        self.__num_atendimentos = 0
        

    @property
    def matricula_coren(self):
        return self.__matricula_coren

    @matricula_coren.setter
    def matricula_coren(self, matricula_coren):
        self.__matricula_coren = matricula_coren

    @property
    def num_atendimentos(self):
        return self.__num_atendimentos
    
    @num_atendimentos.setter
    def num_atendimentos(self, num_atendimentos):
        self.__num_atendimentos = num_atendimentos
