class DiaSemana:

    def __init__(self, nome: str):
        self.__nome = nome
        self.__qtd_pessoas: int


    @property
    def nome(self):
        return self.__nome

    @property
    def qtd_pessoas(self):
        return self.__qtd_pessoas

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @qtd_pessoas.setter
    def qtd_pessoas(self, qtd_pessoas):
        self.__qtd_pessoas = qtd_pessoas