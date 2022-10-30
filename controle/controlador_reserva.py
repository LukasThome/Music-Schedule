from limite.tela_reserva import TelaReserva
from entidade.reserva import Reserva

from random import randint

#ATENÇAO! Nesta classe não estão sendo tratados todos os possíveis problemas.
#é necessário fazer tratamento de exceções em todos os casos!
class ControladorReservas():

  def __init__(self, controlador_sistema):
    self.__controlador_sistema = controlador_sistema
    self.__reservas = []
    self.__tela_reserva = TelaReserva()

  def pega_reserva_por_codigo(self, codigo: int):
    for reserva in self.__reservas:
      if(reserva.codigo == codigo):
        return reserva
    return None

  #Sugestao: listar apenas os bandas que não estão emprestados
  def incluir_reserva(self):
    self.__controlador_sistema.controlador_clientes.lista_clientes()
    self.__controlador_sistema.controlador_bandas.lista_banda()
    dados_reserva = self.__tela_reserva.pega_dados_reserva()

    cliente = self.__controlador_sistema.controlador_clientes.pega_cliente_por_cpf(dados_reserva["cpf"])
    banda = self.__controlador_sistema.controlador_bandas.pega_banda_por_telefone(dados_reserva["telefone"])
    numero_pessoas = int(dados_reserva["numero_pessoas"])


    codigo = randint(0, 100)
    reserva = Reserva(cliente, banda, codigo, numero_pessoas)
    self.__reservas.append(reserva)

  #Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia
  def lista_reserva(self):
    for r in self.__reservas:
      self.__tela_reserva.mostra_reserva({"codigo": r.codigo,
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
      self.__tela_reserva.mostra_mensagem("ATENCAO: Reserva não existente")

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_reserva, 2: self.lista_reserva, 3: self.excluir_reserva,0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_reserva.tela_opcoes()]()
