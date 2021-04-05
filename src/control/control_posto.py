from ..model.posto import Posto
from ..view.tela_posto import PostoView

class PostoController:

    def __init__(self):
        self.__view = PostoView()

    def incluir(self):
        nome = self.__view.incluir()
        return Posto(nome)
