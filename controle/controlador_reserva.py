from limite.tela_reserva import TelaReserva
from entidade.reserva import Reserva

from random import randint

class ControladorReservas():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__reservas = []
        self.__tela_reserva = TelaReserva()
    
    # pegar reserva por dia da semana e contabiliza o total de clientes
    def pega_reserva_por_codigo(self, codigo: int):
        for reserva in self.__reservas:
            if (reserva.codigo == codigo):
                return reserva
        return None
    
    def pega_reserva_por_dia_semana(self, dia_semana):
        contador = 0
        for reserva in self.__reservas:
            if (reserva.dia_semana == dia_semana):
                contador += reserva.numero_pessoas
        return contador

    def incluir_reserva(self):

        # faz um print de todos os clientes
        self.__controlador_sistema.controlador_clientes.lista_clientes()

        self.__controlador_sistema.controlador_agenda.lista_agenda()

        dados_reserva = self.__tela_reserva.pega_dados_reserva()

        dia_semana = dados_reserva["dia_semana"]
        cliente = self.__controlador_sistema.controlador_clientes.pega_cliente_por_cpf(
            dados_reserva["cpf"])
        numero_pessoas = int(dados_reserva["numero_pessoas"])

        codigo = randint(0, 100)
        reserva = Reserva(cliente, codigo, numero_pessoas, dia_semana)
        self.__reservas.append(reserva)

    # Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia
    def lista_reserva(self):
        for r in self.__reservas:
            self.__tela_reserva.mostra_reserva({"codigo": r.codigo,
                                                "dia_semana": r.dia_semana,
                                                "nome_cliente": r.cliente.nome,
                                                "cpf_cliente": r.cliente.cpf,
                                                "numero_pessoas": r.numero_pessoas
                                                })

    def excluir_reserva(self):
        self.lista_reserva()
        codigo_reserva = self.__tela_reserva.seleciona_reserva()
        reserva = self.pega_reserva_por_codigo(int(codigo_reserva))

        if (reserva is not None):
            self.__reservas.remove(reserva)
            self.lista_reserva()
        else:
            self.__tela_reserva.mostra_mensagem(
                "ATENCAO: Reserva não existente")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_reserva, 2: self.lista_reserva,
                        3: self.excluir_reserva, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_reserva.tela_opcoes()]()
