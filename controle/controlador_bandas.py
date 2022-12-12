from limite.tela_banda import TelaBanda
from entidade.banda import Banda
from exceptions.bandaDuplicada import BandaDuplicadaException
from exceptions.bandaNaoExistente import BandaNaoExistenteException
from exceptions.bandaListaVazia import BandaListaVaziaException
from DAOs.banda_dao import BandaDAO



class ControladorBandas():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__banda_DAO = BandaDAO()
       

        self.__tela_banda = TelaBanda()

    def pega_banda_por_telefone(self, telefone: str):
        for banda in self.__banda_DAO.get_all():
        
            if (banda.telefone == telefone):
                return banda
        return None

    def incluir_banda(self):
        dados_banda = self.__tela_banda.pega_dados_banda()
        banda = self.pega_banda_por_telefone(dados_banda["telefone"])
        
        void = bool
        
        if dados_banda["nome"] == "" or dados_banda["telefone"] == "" or dados_banda["estilo"] == "":
            void = True
        else:
            void = False

        try:
            if banda == None and void == False:
                banda = Banda(
                    dados_banda["nome"], dados_banda["telefone"], dados_banda["estilo"])
            
                self.__banda_DAO.add(banda)
            else:
                raise BandaDuplicadaException
        except BandaDuplicadaException as e:
            self.__tela_banda.mostra_mensagem(e)
        
        

    def alterar_banda(self):
        self.lista_banda()
        telefone_banda = self.__tela_banda.seleciona_banda()
        banda = self.pega_banda_por_telefone(telefone_banda)

        try:
            if (banda is not None):
                novos_dados_banda = self.__tela_banda.pega_dados_banda()
                banda.nome = novos_dados_banda["nome"]
                banda.telefone = novos_dados_banda["telefone"]
                banda.estilo = novos_dados_banda["estilo"]
                self.__banda_DAO.update(banda)
                self.lista_banda()
                
            else:
                raise BandaNaoExistenteException

        except BandaNaoExistenteException as e:
             self.__tela_banda.mostra_mensagem(e)

    def lista_banda(self):

        try:
            if len(self.__banda_DAO.get_all()) != 0:
                dados_bandas = []
                
                for banda in self.__banda_DAO.get_all():
                
                    dados_bandas.append({"nome": banda.nome, "telefone": banda.telefone, "estilo": banda.estilo})
                self.__tela_banda.mostra_banda(dados_bandas)               
                
                    
            else:
                raise BandaListaVaziaException
        except BandaListaVaziaException as e:
            self.__tela_banda.mostra_mensagem(e)


    def excluir_banda(self):
        self.lista_banda()
        telefone_banda = self.__tela_banda.seleciona_banda()
        banda = self.pega_banda_por_telefone(telefone_banda)
        try:
            if (banda is not None):
                self.__banda_DAO.remove(banda.telefone)
               
                self.lista_banda()
            else:
                raise BandaNaoExistenteException
        except BandaNaoExistenteException as e:
            self.__tela_banda.mostra_mensagem(e)

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_banda, 2: self.alterar_banda,
                        3: self.lista_banda, 4: self.excluir_banda, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_banda.tela_opcoes()]()
