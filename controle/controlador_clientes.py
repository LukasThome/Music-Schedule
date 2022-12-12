from limite.tela_cliente import TelaCliente
from entidade.cliente import Cliente
from exceptions.clienteDuplicado import ClienteDuplicadaException
from exceptions.clienteNaoExistente import ClienteNaoExistenteException
from exceptions.clienteListaVazia import ClienteListaVaziaException
from DAOs.cliente_dao import ClienteDAO


class ControladorClientes():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__cliente_DAO = ClienteDAO()
 
        self.__tela_cliente = TelaCliente()
        

    def pega_cliente_por_cpf(self, cpf: str):
        
        for cliente in self.__cliente_DAO.get_all():
            if (cliente.cpf == cpf):
                return cliente
            return None

    def incluir_cliente(self):
        dados_cliente = self.__tela_cliente.pega_dados_cliente()
        cliente = self.pega_cliente_por_cpf(dados_cliente["cpf"])
        
        void = False
        
        if dados_cliente["nome"] == "" or dados_cliente["telefone"] == "" or dados_cliente["cpf"] == "":
            void = True

        try:
            if cliente == None and void == False:
                cliente = Cliente(
                    dados_cliente["nome"], dados_cliente["telefone"], dados_cliente["cpf"])
                self.__cliente_DAO.add(cliente)
            else:
                raise ClienteDuplicadaException
        except ClienteDuplicadaException as e:
            self.__tela_cliente.mostra_mensagem(e)

    def alterar_cliente(self):
        self.lista_clientes()
        cpf_cliente = self.__tela_cliente.seleciona_cliente()
        cliente = self.pega_cliente_por_cpf(cpf_cliente)
        try:
            if (cliente is not None):
                novos_dados_cliente = self.__tela_cliente.pega_dados_cliente()
                cliente.nome = novos_dados_cliente["nome"]
                cliente.telefone = novos_dados_cliente["telefone"]
                cliente.cpf = novos_dados_cliente["cpf"]#nao deve ser alterado
                
                self.__cliente_DAO.update(cliente)
                self.lista_clientes()
            else:
                raise ClienteNaoExistenteException
        except ClienteNaoExistenteException as e:
             self.__tela_cliente.mostra_mensagem(e)

    
    def lista_clientes(self):
        try:
            if len(self.__cliente_DAO.get_all()) != 0:
                dados_clientes = []
            
                for cliente in self.__cliente_DAO.get_all():
                    dados_clientes.append({"nome": cliente.nome, "telefone": cliente.telefone, "cpf": cliente.cpf})
                    self.__tela_cliente.mostra_cliente(dados_clientes)

            else:
                raise ClienteListaVaziaException
        except ClienteListaVaziaException as e:
            self.__tela_cliente.mostra_mensagem(e)
               

    def excluir_cliente(self):
        self.lista_clientes()
        cpf_cliente = self.__tela_cliente.seleciona_cliente()
        cliente = self.pega_cliente_por_cpf(cpf_cliente)
        
        try:
            if (cliente is not None):
        
                self.__cliente_DAO.remove(cliente.cpf)
                self.lista_clientes()
            else:
                raise ClienteNaoExistenteException
        except ClienteNaoExistenteException as e:
            self.__tela_cliente.mostra_mensagem(e)

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_cliente, 2: self.alterar_cliente,
                        3: self.lista_clientes, 4: self.excluir_cliente, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_cliente.tela_opcoes()]()
