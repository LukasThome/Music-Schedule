from entidade.relatorio import Relatorio
from limite.tela_relatorio import TelaRelatorio
from exceptions.relatorioNaoExistente import RelatorioNaoExistenteException
from exceptions.relatorioListaVazia import RelatorioListaVaziaException
from exceptions.reservaDiaInvalido import ReservaDiaInvalidoException
from exceptions.agendaNaoExistente import AgendaNaoExistenteException
from DAOs.relatorio_dao import RelatorioDAO

class ControladorRelatorio():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        #self.__relatorios = []
        self.__tela_relatorio = TelaRelatorio()
        self.__relatorio_DAO = RelatorioDAO()
    
    def criar_relatorio(self):
        # mostra a relatorio
        # self.__controlador_sistema.controlador_relatorio.lista_relatorio()
        # vai pegar os dados do usuario
        dados_relatorio = self.__tela_relatorio.pega_dados_relatorio()
        # retorna a variavel dia_semana
        d_semana = dados_relatorio["dia_semana"]


        # calcular o numero de pessoas do respectivo dia da semana ou de todos os dias

        numero_pessoas = self.__controlador_sistema.controlador_reserva.pega_reserva_por_dia_semana(
            d_semana)
        banda = self.__controlador_sistema.controlador_agenda.pega_banda_por_dia_semana(
            d_semana)

        dias_validos = ["SEG", "TER", "QUA", "QUI", "SEX", "SAB", "DOM"]

        print("35",numero_pessoas, banda)

        existe_agenda = bool
        dia_valido = bool
        
        try:
            if d_semana in dias_validos:
                dia_valido = True
            else:
                dia_valido = False
                raise ReservaDiaInvalidoException
        except ReservaDiaInvalidoException as e:
            self.__tela_relatorio.mostra_mensagem(e)
        
        try:
            if banda is not None:
                existe_agenda = True
            else:
                existe_agenda = False
                raise AgendaNaoExistenteException
        except AgendaNaoExistenteException as e:
            self.__tela_relatorio.mostra_mensagem(e)

        

        if dia_valido == True and existe_agenda == True:
            relatorio = Relatorio(d_semana, numero_pessoas, banda)
            self.__relatorio_DAO.add(relatorio)
            print("UEBA")
            #self.__relatorios.append(relatorio)

    def lista_relatorio(self):
            
        try:
            if len(self.__relatorio_DAO.get_all()) != 0:
                dados_relatorios = []
                for relatorio in self.__relatorio_DAO.get_all():
                    
                    dados_relatorios.append({"dia_semana": relatorio.dia_semana, "numero_pessoas": relatorio.numero_pessoas, "nome_banda": relatorio.banda.nome})
                
                self.__tela_relatorio.mostra_relatorio(dados_relatorios)
            else:
                raise RelatorioListaVaziaException
        except RelatorioListaVaziaException as e:
            self.__tela_relatorio.mostra_mensagem(e)


    def pega_relatorio_por_dia_semana(self, dia_semana):
        for relatorio in self.__relatorio_DAO.get_all():
            if (relatorio.dia_semana == dia_semana):
                return relatorio
        return None

    def excluir_relatorio(self):
        self.lista_relatorio()

        dados_relatorio = self.__tela_relatorio.pega_dados_relatorio()
        dia_semana = dados_relatorio["dia_semana"]
        

        relatorio = self.pega_relatorio_por_dia_semana(dia_semana)
        
        dias_validos = ["SEG", "TER", "QUA", "QUI", "SEX", "SAB", "DOM"]
        
        try:
            if dia_semana not in dias_validos:
                raise ReservaDiaInvalidoException
            else:
                pass
        except ReservaDiaInvalidoException as e:
            self.__tela_relatorio.mostra_mensagem(e)
        
        
        try:
            if (relatorio is not None):
                self.__relatorio_DAO.remove(relatorio.dia_semana)
                self.lista_relatorio()
            else:
                raise RelatorioNaoExistenteException
        except RelatorioNaoExistenteException as e:
            self.__tela_relatorio.mostra_mensagem(e)       

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.criar_relatorio,  2: self.lista_relatorio,
                        3: self.excluir_relatorio, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_relatorio.tela_opcoes()]()
