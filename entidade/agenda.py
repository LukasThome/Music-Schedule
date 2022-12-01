from entidade.banda import Banda

class Agenda:

    def __init__(self, banda: Banda, dia_semana: str):

        if (isinstance(banda, Banda)):
            self.__banda = banda

            self.__dia_semana = dia_semana

    @property
    def banda(self):
        return self.__banda

    @property
    def dia_semana(self):
        return self.__dia_semana

    @banda.setter
    def banda(self, banda):
        self.__banda = banda

    @dia_semana.setter
    def dia_semana(self, dia_semana):
        self.__dia_semana = dia_semana