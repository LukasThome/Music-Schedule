import PySimpleGUI as sg

class TelaReserva():
    
    
    def __init__(self):
        self.__window = None
        self.init_opcoes()
    
    # Tratamento de dados
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
    
    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.__window.Read()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
 
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
            [sg.Text('-------- RESERVAS ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Nova Reserva', "RD1", key='1')],
            [sg.Radio('Mostrar Reservas', "RD1", key='2')],
            [sg.Radio('Cancelar Reserva', "RD1", key='3')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Bar Manager').Layout(layout)
    
    
    def pega_dados_reserva(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- DADOS RESERVA ----------', font=("Helvica", 25))],
            [sg.Text('Dia da semana:', size=(15, 1)), sg.InputText('', key='dia_semana')],
            [sg.Text('CPF do cliente:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Text('Número de Pessoas da reserva:', size=(15, 1)), sg.InputText('', key='numero_pessoas')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Bar Manager').Layout(layout)

        button, values = self.open()
        dia_semana = values['dia_semana']
        cpf = values['cpf']
        numero_pessoas = values['numero_pessoas']

        self.close()
        return {"dia_semana": dia_semana, "cpf": cpf, "numero_pessoas": numero_pessoas}
    
    def mostra_reserva(self, dados_reserva):
        string_todas_reservas = ""
        for dado in dados_reserva:
            string_todas_reservas = string_todas_reservas + "CODIGO DA RESERVA: " + dado["codigo"] + '\n'
            string_todas_reservas = string_todas_reservas + "NOME DO CLIENTE: " + dado["nome_cliente"] + '\n'
            string_todas_reservas = string_todas_reservas + "CPF DO CLIENTE: " + str(dado["cpf_cliente"]) + '\n'
            string_todas_reservas = string_todas_reservas + "DIA DA SEMANA: " + str(dado["dia_semana"]) + '\n'
            string_todas_reservas = string_todas_reservas + "NUMERO DE PESSOAS: " + str(dado["numero_pessoas"]) + '\n\n'

        sg.Popup('-------- LISTA DE RESERVAS ----------', string_todas_reservas)


    def seleciona_reserva(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- SELECIONAR RESERVA ----------', font=("Helvica", 25))],
            [sg.Text('Digite o codigo do reserva que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('CODIGO:', size=(15, 1)), sg.InputText('', key='codigo')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona reserva').Layout(layout)

        button, values = self.open()
        codigo = values['codigo']
        self.close()
        return codigo

    def mostra_mensagem(self, msg):
        print(msg)
    
    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values