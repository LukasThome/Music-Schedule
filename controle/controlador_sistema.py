from limite.tela_sistema import TelaSistema
from controle.controlador_clientes import ControladorClientes
from controle.controlador_bandas import ControladorBandas
from controle.controlador_emprestimo import ControladorEmprestimos

class ControladorSistema:

    def __init__(self):
        self.__controlador_bandas = ControladorBandas(self)
        self.__controlador_clientes = ControladorClientes(self)
        self.__controlador_emprestimos = ControladorEmprestimos(self)
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_clientes(self):
        return self.__controlador_clientes

    @property
    def controlador_bandas(self):
        return self.__controlador_bandas

    def inicializa_sistema(self):
        self.abre_tela()

    def cadastra_bandas(self):
        self.__controlador_bandas.abre_tela()

    def cadastra_clientes(self):
        # Chama o controlador de clientes
        self.__controlador_clientes.abre_tela()

    def cadastra_emprestimos(self):
        self.__controlador_emprestimos.abre_tela()
        # Chama o controlador de Emprestimos

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_bandas, 2: self.cadastra_clientes, 3: self.cadastra_emprestimos,
                        0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()