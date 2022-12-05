import PySimpleGUI as sg



class TelaRelatorio():

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
        button, values = self.__window.Read()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        # cobre os casos de Retornar, fechar janela, ou clicar cancelar
        # Isso faz com que retornemos a tela do sistema caso qualquer uma dessas coisas aconteca
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def init_opcoes(self):
        # sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- RELATORIO ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Criar Relatório', "RD1", key='1')],
            [sg.Radio('Mostrar Relatório', "RD1", key='2')],
            [sg.Radio('Deletar Relatório', "RD1", key='3')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Bar Manager').Layout(layout)

        # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
        # opção de tratamento: adicionar um if e só coletar nome e telefone se o button é 'Confirmar'

    def pega_dados_relatorio(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- DADOS RELATÓRIO ----------', font=("Helvica", 25))],
            [sg.Text('Dia da Semana:', size=(15, 1)),
             sg.InputText('', key='dia_semana')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Bar Manager').Layout(layout)

        button, values = self.open()
        dia_semana = values['dia_semana']

        self.close()
        return {"dia_semana": dia_semana}


    def mostra_relatorio(self, dados_relatorio):
        string_todos_relatorios = ""
        for dado in dados_relatorio:
            string_todos_relatorios = string_todos_relatorios + \
                "DIA DA SEMANA: " + dado["dia_semana"] + '\n'
            string_todos_relatorios = string_todos_relatorios + \
                "BANDA: " + str(dado["nome_banda"]) + '\n'
            string_todos_relatorios = string_todos_relatorios + \
                "NUMERO DE PESSOAS: " + str(dado["numero_pessoas"]) + '\n\n'

        sg.Popup('-------- RELATÓRIO ----------', string_todos_relatorios)

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado

    def mostra_mensagem(self, msg):
        print(msg)

    def close(self):
        self.__window.Close()
    
    def open(self):
        button, values = self.__window.Read()
        return button, values