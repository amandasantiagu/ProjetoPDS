class Posto:

    def __init__(self, nome):
        self.__nome = nome
        self.__total_doses = 0


    @property
    def total_doses():
        return self.__total_doses


    @property
    def nome(self):
        return self.__nome


    def novas_doses(num):
        total_doses = total_doses + num
