import PySimpleGUI as sg

class TelaCliente():
    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado

    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def le_num_inteiro(self, mensagem=" ", ints_validos=None):
        while True:
            valor_lido = input(mensagem)
            try:
                # tenta transformar o valor lido em inteiro.
                valor_int = int(valor_lido)
                if ints_validos and valor_int not in ints_validos:
                    raise ValueError  # será lançada apenas se o número não é o esperado
                return valor_int
            except ValueError:  # aqui cai se não for int ou se não for valido
                print("Valor incorreto!")
                if ints_validos:
                    print("Valores válidos: ", ints_validos)

      # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.open()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        # cobre os casos de Retornar, fechar janela, ou clicar cancelar
        #Isso faz com que retornemos a tela do sistema caso qualquer uma dessas coisas aconteca
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao        
    

    def init_opcoes(self):
    # sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- CLIENTES ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Incluir Cliente', "RD1", key='1')],
            [sg.Radio('Alterar Cliente', "RD1", key='2')],
            [sg.Radio('Listar Clientes', "RD1", key='3')],
            [sg.Radio('Excluir Cliente', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Bar Manager').Layout(layout)

    def init_opcoes(self):
        # sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- CLIENTES ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Incluir Cliente', "RD1", key='1')],
            [sg.Radio('Alterar Cliente', "RD1", key='2')],
            [sg.Radio('Listar Clientes', "RD1", key='3')],
            [sg.Radio('Excluir Cliente', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Bar Manager').Layout(layout)

# fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
# opção de tratamento: adicionar um if e só coletar nome e telefone se o button é 'Confirmar'
    def pega_dados_cliente(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('-------- DADOS CLIENTE ----------', font=("Helvica", 25))],
        [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
        [sg.Text('Telefone:', size=(15, 1)), sg.InputText('', key='telefone')],
        [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Bar Manager').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        telefone = values['telefone']
        cpf = values['cpf']

        self.close()
        return {"nome": nome, "telefone": telefone, "cpf": cpf}

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def mostra_cliente(self, dados_cliente):
        string_todos_clientes = ""
        for dado in dados_cliente:
            string_todos_clientes = string_todos_clientes + "NOME DO CLIENTE: " + dado["nome"] + '\n'
            string_todos_clientes = string_todos_clientes + "FONE DO CLIENTE: " + str(dado["telefone"]) + '\n'
            string_todos_clientes = string_todos_clientes + "CPF DO CLIENTE: " + str(dado["cpf"]) + '\n\n'

        sg.Popup('-------- LISTA DE CLIENTES ----------', string_todos_clientes)

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def seleciona_cliente(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- SELECIONAR CLIENTE ----------', font=("Helvica", 25))],
            [sg.Text('Digite o CPF do cliente que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona cliente').Layout(layout)

        button, values = self.open()
        cpf = values['cpf']
        self.close()
        return cpf

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
   
   
   
   
   
   
''' def tela_opcoes(self):
        print("\n")
        print("-------- CLIENTES ----------")
        print("Escolha a opcao")
        print("1 - Incluir Cliente")
        print("2 - Alterar Cliente")
        print("3 - Listar Clientes")
        print("4 - Excluir Cliente")
        print("0 - Retornar")

        opcao = self.le_num_inteiro("Escolha a opcao:", [0, 1, 2, 3, 4])

        return opcao

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def pega_dados_cliente(self):
        print("\n")
        print("-------- DADOS CLIENTE ----------")
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        cpf = input("CPF: ")

        print("Cadsatro efetuado com sucesso!")
        print("\n")

        return {"nome": nome, "telefone": telefone, "cpf": cpf}

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado

    def mostra_cliente(self, dados_cliente):
        print("\n")
        print("NOME DO CLIENTE: ", dados_cliente["nome"])
        print("FONE DO CLIENTE: ", dados_cliente["telefone"])
        print("CPF DO CLIENTE: ", dados_cliente["cpf"])
        print("\n")

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def seleciona_cliente(self):
        cpf = input("CPF do cliente que deseja selecionar: ")
        return cpf

    def mostra_mensagem(self, msg):
        print(msg)
'''


