from control.abstractDAO import AbstractDAO
from model.vacina import Vacina


class VacinaDAO(AbstractDAO):
    def __init__(self):
        super().__init__('vacinas.pkl')
    
    def add(self, vacina: Vacina):
        if isinstance(vacina.num_id, int) and (vacina is not None) and isinstance(vacina, Vacina):
            super().add(vacina)
    
    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            super().remove(key)
