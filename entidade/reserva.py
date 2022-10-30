from entidade.cliente import Cliente
from entidade.banda import Banda


class Reserva:
    def __init__(self, cliente: Cliente, banda: Banda, codigo: int, numero_pessoas: int):
        if (isinstance(banda, Banda)):
            self.__banda = banda
        if (isinstance(cliente, Cliente)):
            self.__cliente = cliente

        self.__codigo = codigo
        self.__numero_pessoas = numero_pessoas

    @property
    def cliente(self):
        return self.__cliente

    @property
    def banda(self):
        return self.__banda

    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def numero_pessoas(self):
      return self.__numero_pessoas

    @numero_pessoas.setter
    def numero_pessoas(self, numero_pessoas):
      self.__numero_pessoas = numero_pessoas

    @cliente.setter
    def cliente(self, cliente: Cliente):
        if (isinstance(cliente, Cliente)):
            self.__cliente = cliente

    @banda.setter
    def banda(self, banda: Banda):
        if (isinstance(banda, Banda)):
            self.__banda = banda

    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo
