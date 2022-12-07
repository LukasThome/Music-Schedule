from limite.tela_cliente import TelaCliente
from entidade.cliente import Cliente

# ATENÇAO! Nesta classe não estão sendo tratados todos os possíveis problemas.
# é necessário fazer tratamento de exceções em todos os casos!


class ControladorClientes():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        
        ###clientes pre definidos para teste###
        cliente01 = Cliente("Lucas", "489", "778899")
        cliente02 = Cliente("Leo", "488", "774411")
        cliente03 = Cliente("Luiz", "487", "332211")
        ### ---- ###
        
        self.__clientes = [cliente01, cliente02, cliente03]  
        self.__tela_cliente = TelaCliente()
        

    def pega_cliente_por_cpf(self, cpf: str):
        for cliente in self.__clientes:
            if (cliente.cpf == cpf):
                return cliente
        return None

    # testagem com lançamento de exceção para clientes já existentes!
    def incluir_cliente(self):
        dados_cliente = self.__tela_cliente.pega_dados_cliente()
        cliente = self.pega_cliente_por_cpf(dados_cliente["cpf"])
        try:
            if cliente == None:
                cliente = Cliente(
                    dados_cliente["nome"], dados_cliente["telefone"], dados_cliente["cpf"])
                self.__clientes.append(cliente)
            else:
                raise KeyError
        except KeyError:
            self.__tela_cliente.mostra_mensagem("Cliente já existente!")

    def alterar_cliente(self):
        self.lista_clientes()
        cpf_cliente = self.__tela_cliente.seleciona_cliente()
        cliente = self.pega_cliente_por_cpf(cpf_cliente)

        if (cliente is not None):
            novos_dados_cliente = self.__tela_cliente.pega_dados_cliente()
            cliente.nome = novos_dados_cliente["nome"]
            cliente.telefone = novos_dados_cliente["telefone"]
            cliente.cpf = novos_dados_cliente["cpf"]
            self.lista_clientes()
        else:
            self.__tela_cliente.mostra_mensagem(
                "ATENCAO: Cliente não existente")

    # Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia
    def lista_clientes(self):
        if len(self.__clientes) == 0:
            #Adicionar a classe de exception aqui
            self.__tela_cliente.mostra_mensagem(
                "Nenhum cliente para ser mostrado")
        else:
            dados_clientes = []
            for cliente in self.__clientes:
                dados_clientes.append({"nome": cliente.nome, "telefone": cliente.telefone, "cpf": cliente.cpf})
            self.__tela_cliente.mostra_cliente(dados_clientes)

    def excluir_cliente(self):
        self.lista_clientes()
        cpf_cliente = self.__tela_cliente.seleciona_cliente()
        cliente = self.pega_cliente_por_cpf(cpf_cliente)

        if (cliente is not None):
            self.__clientes.remove(cliente)
            self.lista_clientes()
        else:
            self.__tela_cliente.mostra_mensagem(
                "ATENCAO: Cliente não existente")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_cliente, 2: self.alterar_cliente,
                        3: self.lista_clientes, 4: self.excluir_cliente, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_cliente.tela_opcoes()]()
