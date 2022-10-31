from entidade.relatorio import Relatorio
from limite.tela_relatorio import TelaRelatorio

class ControladorRelatorio():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__relatorios = []    
        self.__tela_relatorio = TelaRelatorio()


    def criar_relatorio(self):
        #mostra a agenda
        self.__controlador_sistema.controlador_agenda.lista_agenda()
        #vai pegar os dados do usuario
        dados_relatorio = self.__tela_relatorio.pega_dados_relatorio()
        #retorna a variavel dia_semana
        dia_semana = dados_relatorio["dia_semana"]

        #calcular o numero de pessoas do respectivo dia da semana ou de todos os dias

        numero_pessoas = self.__controlador_sistema.controlador_reservas.pega_reserva_por_dia_semana(dia_semana)

        relatorio = Relatorio(dia_semana, numero_pessoas)

        self.__relatorios.append(relatorio)
    
    


