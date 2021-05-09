class Vacina():
    def __init__(self, tipo_vacina: str, fabricante: str, quantidade: int, num_registro: int):
        self.__tipo_vacina = tipo_vacina
        self.__fabricante = fabricante
        self.__quantidade = quantidade
        self.__num_registro = num_registro

    @property
    def tipo_vacina(self):
        return self.__tipo_vacina

    @tipo_vacina.setter
    def tipo_vacina(self,tipo_vacina):
        self.__tipo_vacina = tipo_vacina

    @property
    def fabricante(self):
        return self.__fabricante

    @fabricante.setter
    def fabricante(self, fabricante):
        self.__fabricante = fabricante
    
    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade
    
    @property
    def num_registro(self):
        return self.__num_registro

    @num_registro.setter
    def num_registro(self, num_registro):
        self.__num_registro = num_registro
