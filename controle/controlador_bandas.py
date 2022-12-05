from limite.tela_banda import TelaBanda
from entidade.banda import Banda

# ATENÇAO! Nesta classe não estão sendo tratados todos os possíveis problemas.
# é necessário fazer tratamento de exceções em todos os casos!


class ControladorBandas():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        
        ###bandas pre definidas para teste###
        banda01 = Banda("Greta Van Fleet", "112", "Rock")
        banda02 = Banda("The Strokes", "113", "Rock")
        banda03 = Banda("Metallica", "114", "Metal")
        ### ------ ###
        self.__bandas = [banda01, banda02, banda03]
        
        self.__tela_banda = TelaBanda()

    def pega_banda_por_telefone(self, telefone: str):
        for banda in self.__bandas:
            if (banda.telefone == telefone):
                return banda
        return None

    def incluir_banda(self):
        dados_banda = self.__tela_banda.pega_dados_banda()
        banda = Banda(dados_banda["nome"],
                      dados_banda["telefone"], dados_banda["estilo"])

        self.__bandas.append(banda)

    def alterar_banda(self):
        self.lista_banda()
        telefone_banda = self.__tela_banda.seleciona_banda()
        banda = self.pega_banda_por_telefone(telefone_banda)

        if (banda is not None):
            novos_dados_banda = self.__tela_banda.pega_dados_banda()
            banda.nome = novos_dados_banda["nome"]
            banda.telefone = novos_dados_banda["telefone"]
            banda.estilo = novos_dados_banda["estilo"]
            self.lista_banda()
        else:
            self.__tela_banda.mostra_mensagem("ATENCAO: Banda não existente")

    # Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia
    def lista_banda(self):
        if len(self.__bandas) == 0:
            
            #Adicionar a classe de exception aqui
            print("\n")
            print("Lista de bandas vazia")
        else:
            dados_bandas = []
            for banda in self.__bandas:
                #self.__tela_banda.mostra_banda({"nome": banda.nome, "telefone": banda.telefone, "cpf": banda.cpf})
                dados_bandas.append({"nome": banda.nome, "telefone": banda.telefone, "estilo": banda.estilo})
            self.__tela_banda.mostra_banda(dados_bandas)

    def excluir_banda(self):
        self.lista_banda()
        telefone_banda = self.__tela_banda.seleciona_banda()
        banda = self.pega_banda_por_telefone(telefone_banda)

        if (banda is not None):
            self.__bandas.remove(banda)
            self.lista_banda()
        else:
            self.__tela_banda.mostra_mensagem("ATENCAO: Banda não existente")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_banda, 2: self.alterar_banda,
                        3: self.lista_banda, 4: self.excluir_banda, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_banda.tela_opcoes()]()
