from DAOs.dao import DAO
from entidade.agenda import Agenda

class AgendaDAO(DAO):
    def __init__(self):
        super().__init__('agendas.pkl')

    def add(self, agenda: Agenda):
        if((agenda is not None) and isinstance(agenda, Agenda) and isinstance(agenda.dia_semana, str)):
            super().add(agenda.dia_semana, agenda)

    def update(self, agenda: Agenda):
        if((agenda is not None) and isinstance(agenda, Agenda) and isinstance(agenda.dia_semana, str)):
            super().update(agenda.dia_semana, agenda)

    def get(self, key:str):
        if isinstance(key, str):
            return super().get(key)

    def remove(selfself, key:str):
        if(isinstance(key, str)):
            return super().remove(key)