class Vacina():
    def __init__(self, tipo_vacina: str, fabricante: str):
        self.__tipo_vacina = tipo_vacina
        self.__fabricante = fabricante

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