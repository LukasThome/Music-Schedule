from entidade.banda import Banda
from entidade.reserva import Reserva
from entidade.agenda import Agenda

class Relatorio:

    def __init__(self, dia_semana: str, numero_pessoas: int, banda: Banda):
        self.__dia_semana = dia_semana
        self.__numero_pessoas = numero_pessoas
        self.__banda = banda


    @property
    def dia_semana(self):
        return self.__dia_semana

    @property
    def numero_pessoas(self):
        return self.__numero_pessoas

    @property
    def banda(self):
        return self.__banda
    
    @banda.setter
    def banda(self, banda):
        self.__banda = banda

    @dia_semana.setter
    def dia_semana(self, dia_semana):
        self.__dia_semana = dia_semana

    @numero_pessoas.setter
    def numero_pessoas(self, numero_pessoas):
        self.__numero_pessoas = numero_pessoas
    