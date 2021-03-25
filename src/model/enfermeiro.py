
class Enfermeiro():
    def __init__(self, matricula_coren: int, nome_completo: str, cpf: int, data_nascimento:str):
        self.__matricula_coren = matricula_coren
        self.__nome_completo = nome_completo
        self.__data_nascimento = data_nascimento
        self.__cpf = cpf
        self.__num_atendimentos = 0 

    @property
    def matricula_coren(self):
        return self.__matricula_coren

    @matricula_coren.setter
    def matricula_coren(self, matricula_coren):
        self.__matricula_coren = matricula_coren

    @property
    def nome_completo(self):
        return self.__nome_completo

    @nome_completo.setter
    def nome_completo(self, nome_completo):
        self.__nome_completo = nome_completo

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento

    @property
    def cpf(self):
        return self.__cpf
        
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def num_atendimentos(self):
        return self.__num_atendimentos
    
    @num_atendimentos.setter
    def num_atendimentos(self, num_atendimentos):
        self.__num_atendimentos = num_atendimentos
