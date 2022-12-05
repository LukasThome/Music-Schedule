from entidade.relatorio import Relatorio
from limite.tela_relatorio import TelaRelatorio


class ControladorRelatorio():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__relatorios = []
        self.__tela_relatorio = TelaRelatorio()

    def criar_relatorio(self):
        # mostra a agenda
        # self.__controlador_sistema.controlador_agenda.lista_agenda()
        # vai pegar os dados do usuario
        dados_relatorio = self.__tela_relatorio()
        # retorna a variavel dia_semana
        d_semana = dados_relatorio["dia_semana"]

        # calcular o numero de pessoas do respectivo dia da semana ou de todos os dias

        numero_pessoas = self.__controlador_sistema.controlador_reserva.pega_reserva_por_dia_semana(
            d_semana)
        banda = self.__controlador_sistema.controlador_agenda.pega_banda_por_dia_semana(
            d_semana)

        relatorio = Relatorio(d_semana, numero_pessoas, banda)

        self.__relatorios.append(relatorio)

    def lista_relatorio(self):
        for r in self.__relatorios:
            self.__tela_relatorio.mostra_relatorio({"dia_semana": r.dia_semana,
                                                    "numero_pessoas": r.numero_pessoas,
                                                    "nome_banda": r.banda.nome
                                                    })

    def pega_relatorio_por_dia_semana(self, dia_semana):
        for relatorio in self.__relatorios:
            if (relatorio.dia_semana == dia_semana):
                return relatorio
        return None

    def excluir_relatorio(self):
        self.lista_relatorio()

        day_semana = self.__tela_relatorio.pega_dados_relatorio()

        relatorio = self.pega_relatorio_por_dia_semana(day_semana)

        if (relatorio is not None):
            self.__relatorios.remove(relatorio)
            self.lista_relatorio()
        else:
            self.__tela_relatorio.mostra_mensagem(
                "ATENCAO: Relatorio não existente")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.criar_relatorio,  2: self.lista_relatorio,
                        3: self.excluir_relatorio, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_relatorio.tela_opcoes()]()
