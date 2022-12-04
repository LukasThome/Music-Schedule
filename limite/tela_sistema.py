import PySimpleGUI as sg

class TelaSistema:

    def __init__(self):
        self.__window = None
        self.init_components()

    # essa função trata o caso de não digitar um valor valido
    # note que está dentro de um while True. Só sai do loop quando digitado um valor correto
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

    '''def tela_opcoes(self):
        print("\n")
        print("-------- Bar do Python ---------")
        print("Escolha sua opcao")
        print("1 - Bandas")
        print("2 - Clientes")
        print("3 - Reservas")
        print("4 - Agenda Musical")
        print("5 - Relatório")
        print("0 - Finalizar sistema")
        opcao = self.le_num_inteiro("Escolha a opcao:", [0, 1, 2, 3, 4, 5])
        print("\n")
        return opcao
        '''

    def tela_opcoes(self):
        self.init_components()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if values['5']:
            opcao = 5    
        # cobre os casos de voltar, não clicar em nada e fechar janela, ou clicar cancelar
        if values['0'] or button in (None,'Cancelar'):
            opcao = 0
        self.close()
        return opcao
    
    def init_components(self):
        #sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Bar Manager', font=("Helvica",25))],
            [sg.Text('Escolha sua opção', font=("Helvica",15))],
            [sg.Radio('Bandas',"RD1", key='1')],
            [sg.Radio('Clientes',"RD1", key='2')],
            [sg.Radio('Reservas',"RD1", key='3')],
            [sg.Radio('Agenda Musical',"RD1", key='4')],
            [sg.Radio('Relatórios',"RD1", key='5')],
            [sg.Radio('Finalizar sistema',"RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Bar Manager').Layout(layout)
    
    def close(self):
        self.__window.Close()