from entidade.banda import Banda
from entidade.reserva import Reserva
from entidade.agenda import Agenda

class Relatorio:

    def __init__(self, dia_semana: str, numero_pessoas: int):
        self.__dia_semana = dia_semana
        self.__numero_pessoas = numero_pessoas


    @property
    def dia_semana(self):
        return self.__dia_semana

    @property
    def numero_pessoas(self):
        return self.__numero_pessoas

    @dia_semana.setter
    def dia_semana(self, dia_semana):
        self.__dia_semana = dia_semana

    @numero_pessoas.setter
    def numero_pessoas(self, numero_pessoas):
        self.__numero_pessoas = numero_pessoas
    