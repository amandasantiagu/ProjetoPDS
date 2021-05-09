from ..persistence.abstractDAO import AbstractDAO
from ..vacina import Vacina


class VacinaDAO(AbstractDAO):
    def __init__(self):
        super().__init__('vacinas.pkl')
    
    def add(self, vacina: Vacina):
        if isinstance(vacina.num_registro, int) and (vacina is not None) and isinstance(vacina, Vacina):
            super().add(vacina, vacina.num_registro)
    
    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            super().remove(key)
