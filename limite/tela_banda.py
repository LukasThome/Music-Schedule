import PySimpleGUI as sg

class TelaBanda():
    
    def __init__(self):
        self.__window = None
        self.init_opcoes()


    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.__window.Read()
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
            [sg.Text('-------- BANDAS ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Cadastrar Banda', "RD1", key='1')],
            [sg.Radio('Alterar Banda', "RD1", key='2')],
            [sg.Radio('Mostrar Bandas', "RD1", key='3')],
            [sg.Radio('Excluir Banda', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Bar Manager').Layout(layout)
    
    def pega_dados_banda(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- DADOS BANDA ----------', font=("Helvica", 25))],
            [sg.Text('Nome da Banda:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Telefone:', size=(15, 1)), sg.InputText('', key='telefone')],
            [sg.Text('Estilo Musical:', size=(15, 1)), sg.InputText('', key='estilo')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Bar Manager').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        telefone = values['telefone']
        estilo = values['estilo']

        self.close()
        return {"nome": nome, "telefone": telefone, "estilo": estilo}

    def mostra_banda(self, dados_banda):
          
        string_t_bandas = ""
        for dado in dados_banda:
            string_t_bandas = string_t_bandas + "NOME DA BANDA: " + dado["nome"] + '\n'
            string_t_bandas = string_t_bandas + "TELEFONE: " + dado["telefone"] + '\n'
            string_t_bandas = string_t_bandas + "ESTILO MUSICAL: " + str(dado["estilo"]) + '\n\n'
        

        sg.Popup('-------- LISTA DE BANDAS ----------', string_t_bandas)
    
    
    def seleciona_banda(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- SELECIONAR BANDA ----------', font=("Helvica", 25))],
            [sg.Text('Digite o telefone do banda que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('TELEFONE:', size=(15, 1)), sg.InputText('', key='telefone')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona banda').Layout(layout)

        button, values = self.__window.Read()
        telefone = values['telefone']
        self.close()
        return telefone


    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    
    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values