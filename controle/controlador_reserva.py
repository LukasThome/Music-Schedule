from limite.tela_reserva import TelaReserva
from entidade.reserva import Reserva
from exceptions.reservaDiaInvalido import ReservaDiaInvalidoException
from exceptions.reservaListaVazia import ReservaListaVaziaException
from exceptions.reservaNaoExistente import ReservaNaoExistenteException
from exceptions.inteiroInvalido import  InteiroInvalidopException
from exceptions.clienteNaoExistente import ClienteNaoExistenteException
from exceptions.agendaListaVazia import AgendaListaVaziaException
from DAOs.reserva_dao import ReservaDAO



from random import randint

class ControladorReservas():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__reserva_DAO = ReservaDAO()

        ###reservas pre-definidas para teste###
        #cliente = self.__controlador_sistema.controlador_clientes.pega_cliente_por_cpf("778899")
        #reserva01 = Reserva(cliente, "777", 6, "TER")
        #cliente = self.__controlador_sistema.controlador_clientes.pega_cliente_por_cpf("774411")
        #reserva02 = Reserva(cliente, "888", 3, "QUA")
        #cliente = self.__controlador_sistema.controlador_clientes.pega_cliente_por_cpf("774411")
        #reserva03 = Reserva(cliente, "999", 4, "QUI")
        ### ------------------ ###
    
        #self.__reservas = [reserva01, reserva02, reserva03]
        
        self.__tela_reserva = TelaReserva()
    
    # pegar reserva por dia da semana e contabiliza o total de clientes
    def pega_reserva_por_codigo(self, codigo: str):
        for reserva in self.__reserva_DAO.get_all():
        #for reserva in self.__reservas:
            if (reserva.codigo == codigo):
                return reserva
        return None
    
    #pega reserva por dia da semana e ja retorna o numero total de pessoas
    def pega_reserva_por_dia_semana(self, dia_semana: str):
        contador = 0
        for reserva in self.__reserva_DAO.get_all():
            if (reserva.dia_semana == dia_semana):
                contador += reserva.numero_pessoas
        return contador

    def incluir_reserva(self):

        # faz um print de todos os clientes
        self.__controlador_sistema.controlador_clientes.lista_clientes()

       
        self.__controlador_sistema.controlador_agenda.lista_agenda()

        

        dados_reserva = self.__tela_reserva.pega_dados_reserva()
        dias_validos = ["SEG", "TER", "QUA", "QUI", "SEX", "SAB", "DOM"]
        dia_semana = dados_reserva["dia_semana"]


        cliente = self.__controlador_sistema.controlador_clientes.pega_cliente_por_cpf(
                    dados_reserva["cpf"])
        
        codigo = randint(0, 100)
        
        ehInteiro = bool
        dia_valido = bool
        existe_cliente = bool

        ##verifica se é int o valor de numero pessoas
        try:    
            numero_pessoas = int(dados_reserva["numero_pessoas"])
            ehInteiro = True   
        except ValueError:
            ehInteiro = False
            self.__tela_reserva.mostra_mensagem("Insira um valor inteiro")



        ##verifica se o usuario digitou o dia da semana corretamente
        try:
            if dia_semana in dias_validos:
               dia_valido = True
            else:
                raise ReservaDiaInvalidoException
        except ReservaDiaInvalidoException as e:
            self.__tela_reserva.mostra_mensagem(e)

        ##verifica se o cliente é existente
        try:
            if cliente is not None:
                existe_cliente = True
            else:
                existe_cliente = False
                raise ClienteNaoExistenteException
        except ClienteNaoExistenteException as e:
            self.__tela_reserva.mostra_mensagem(e)


        
        if ehInteiro == True and dia_valido == True and existe_cliente == True:
            reserva = Reserva(cliente, str(codigo), numero_pessoas, dia_semana)
            self.__reserva_DAO.add(reserva)
            #self.__reservas.append(reserva)
            

    # Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia
    def lista_reserva(self):
        try:
            if len(self.__reserva_DAO.get_all()) != 0:
                dados_reservas = []
                for reserva in self.__reserva_DAO.get_all():
                    dados_reservas.append({"codigo": reserva.codigo, "dia_semana": reserva.dia_semana, "nome_cliente": reserva.cliente.nome, "cpf_cliente": reserva.cliente.cpf, "numero_pessoas": reserva.numero_pessoas})
                self.__tela_reserva.mostra_reserva(dados_reservas)
            else:
                raise ReservaListaVaziaException
        except ReservaListaVaziaException as e:
            self.__tela_reserva.mostra_mensagem(e)
            
           
    def excluir_reserva(self):
        self.lista_reserva()
        codigo_reserva = self.__tela_reserva.seleciona_reserva()
        reserva = self.pega_reserva_por_codigo(codigo_reserva)
        try:
            if (reserva is not None):
                self.reserva.remove(reserva.codigo)
               # self.__reservas.remove(reserva)
                self.lista_reserva()
            else:
                raise ReservaNaoExistenteException
        except ReservaNaoExistenteException as e:
            self.__tela_reserva.mostra_mensagem(e)

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_reserva, 2: self.lista_reserva,
                        3: self.excluir_reserva, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_reserva.tela_opcoes()]()
