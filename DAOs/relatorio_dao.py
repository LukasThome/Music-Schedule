from DAOs.dao import DAO
from entidade.relatorio import Relatorio

class RelatorioDAO(DAO):
    def __init__(self):
        super().__init__('relatorios.pkl')

    def add(self, relatorio: Relatorio):
        if((relatorio is not None) and isinstance(relatorio, Relatorio) and isinstance(relatorio.dia_semana, str)):
            super().add(relatorio.dia_semana, relatorio)

    def update(self, relatorio: Relatorio):
        if((relatorio is not None) and isinstance(relatorio, Relatorio) and isinstance(relatorio.dia_semana, str)):
            super().update(relatorio.dia_semana, relatorio)

    def get(self, key:str):
        if isinstance(key, str):
            return super().get(key)

    def remove(selfself, key:str):
        if(isinstance(key, str)):
            return super().remove(key)