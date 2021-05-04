from ..persistence.abstractDAO import AbstractDAO
from ..posto import Posto


class PostoDAO(AbstractDAO):
    def __init__(self):
        super().__init__('posto.pkl')
    
    def add(self, posto: Posto):
        if (posto is not None) and isinstance(posto, Posto):
            super().add(posto, 1)
    
    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            super().remove(key)
