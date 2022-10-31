from limite.tela_sistema import TelaSistema
from controle.controlador_clientes import ControladorClientes
from controle.controlador_bandas import ControladorBandas
from controle.controlador_reserva import ControladorReservas
from controle.controlador_agenda import ControladorAgenda
from controle.controlador_relatorio import ControladorRelatorio

class ControladorSistema:

    def __init__(self):
        self.__controlador_bandas = ControladorBandas(self)
        self.__controlador_clientes = ControladorClientes(self)
        self.__controlador_reservas = ControladorReservas(self)
        self.__controlador_agenda = ControladorAgenda(self)
        self.__controlador_relatorio = ControladorRelatorio(self)
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_clientes(self):
        return self.__controlador_clientes

    @property
    def controlador_bandas(self):
        return self.__controlador_bandas
    
    @property
    def controlador_agenda(self):
        return self.__controlador_agenda
    @property
    def controlador_relatorio(self):
        return self.__controlador_relatorio
    @property
    def controlador_reserva(self):
        return self.__controlador_reservas

    def inicializa_sistema(self):
        self.abre_tela()

    def cadastra_bandas(self):
        self.__controlador_bandas.abre_tela()

    def cadastra_clientes(self):
        # Chama o controlador de clientes
        self.__controlador_clientes.abre_tela()

    def cadastra_reservas(self):
        self.__controlador_reservas.abre_tela()
        # Chama o controlador de ReserControladorReservas

    def cadastra_agenda(self):
        self.__controlador_agenda.abre_tela()

    def criar_relatorio(self):
        self.__controlador_relatorio.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_bandas, 2: self.cadastra_clientes, 3: self.cadastra_reservas,
                        4: self.cadastra_agenda, 5: self.criar_relatorio, 0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()