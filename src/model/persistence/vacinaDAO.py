from control.abstractDAO import AbstractDAO
from model.vacina import Vacina


class VacinaDAO(AbstractDAO):
    def __init__(self):
        super().__init__('vacinas.pkl')
    
    def add(self, vacina: Vacina):
        if (vacina is not None) and isinstance(vacina, Vacina):
            vacina.num_id = super().gen_id()
            super().add(vacina, vacina.num_id)
    
    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            super().remove(key)
