from control.abstractDAO import AbstractDAO
from model.enfermeiro import Enfermeiro


class EnfermeiroDAO(AbstractDAO):
    def __init__(self):
        super().__init__('enfermeiros.pkl')
    
    def add(self, enfermeiro: Enfermeiro):
        if isinstance(enfermeiro.matricula_coren, int) and (enfermeiro is not None) and isinstance(enfermeiro, Enfermeiro):
            super().add(enfermeiro, enfermeiro.matricula_coren)
    
    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            super().remove(key)
