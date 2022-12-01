from entidade.cliente import Cliente

class Reserva:
    def __init__(self, cliente: Cliente, codigo: int, numero_pessoas: int, dia_semana: str):

        if (isinstance(cliente, Cliente)):
            self.__cliente = cliente

        self.__codigo = codigo
        self.__numero_pessoas = numero_pessoas
        self.__dia_semana = dia_semana

    @property
    def cliente(self):
        return self.__cliente

    @property
    def codigo(self):
        return self.__codigo

    @property
    def numero_pessoas(self):
        return self.__numero_pessoas

    @property
    def dia_semana(self):
        return self.__dia_semana

    @dia_semana.setter
    def dia_semana(self, dia_semana):
        self.__dia_semana = dia_semana

    @numero_pessoas.setter
    def numero_pessoas(self, numero_pessoas):
        self.__numero_pessoas = numero_pessoas

    @cliente.setter
    def cliente(self, cliente: Cliente):
        if (isinstance(cliente, Cliente)):
            self.__cliente = cliente

    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo
