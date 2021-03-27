
class Enfermeiro():

    def __init(self, nome_completo, cpf, idade, endereco, matricula_coren, num_atendimentos):
        self.__matricula_coren = matricula_coren
        self.__num_atendimentos = num_atendimentos
        super(nome_completo, cpf, idade, endereco)


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
