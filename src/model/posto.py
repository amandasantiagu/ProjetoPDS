class Posto:

    def __init__(self, name):
        self.__name = name
        self.__total_doses = 0


    @property
    def total_doses():
        return self.__total_doses


    def novas_doses(num):
        total_doses = total_doses + num
