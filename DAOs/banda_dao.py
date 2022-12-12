from DAOs.dao import DAO
from entidade.banda import Banda

#cada entidade terá uma classe dessa, implementação bem simples.
class BandaDAO(DAO):
    def __init__(self):
        super().__init__('bandas.pkl')

    def add(self, banda: Banda):
        if((banda is not None) and isinstance(banda, Banda) and isinstance(banda.telefone, str)):
            super().add(banda.telefone, banda)

    def update(self, banda: Banda):
        if((banda is not None) and isinstance(banda, Banda) and isinstance(banda.telefone, str)):
            super().update(banda.telefone, banda)

    def get(self, key:str):
        if isinstance(key, str):
            return super().get(key)

    def remove(selfself, key:str):
        if(isinstance(key, str)):
            return super().remove(key)