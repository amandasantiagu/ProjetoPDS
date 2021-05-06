from ..model.posto import Posto
from ..view.posto_view import PostoView
from ..model.persistence.postoDAO import PostoDAO

class PostoController:

    def __init__(self):
        self.__view = PostoView()
        self.__postoDAO= PostoDAO()
        self.__posto = self.__postoDAO.get(1)
        if self.__posto is None:
            self.__posto = Posto("Santiago&Moreira")
            self.__postoDAO.add(self.__posto)
            
    @property
    def posto(self):
        return self.__posto

    def incluir(self):
        nome = self.__view.incluir()
        self.__posto.nome = nome
        self.__postoDAO.update(1, self.__posto)