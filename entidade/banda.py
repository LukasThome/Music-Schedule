class Banda:

    def __init__(self, nome: str,  telefone: int, estilo: str):
        self.__nome = nome
        self.__estilo = estilo
        self.__telefone = telefone
        

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def estilo(self):
        return self.__estilo

    @estilo.setter
    def estilo(self, estilo):
        self.__estilo = estilo

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

