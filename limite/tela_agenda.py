import PySimpleGUI as sg

class TelaAgenda():

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
            [sg.Text('-------- AGENDA ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Criar Agenda', "RD1", key='1')],
            [sg.Radio('Mostrar Agenda', "RD1", key='2')],
            [sg.Radio('Excluir Agenda', "RD1", key='3')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Bar Manager').Layout(layout)
    
    def pega_dados_agenda(self):

        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- DADOS AGENDA ----------', font=("Helvica", 25))],
            [sg.Text('Dia da Semana:', size=(15, 1)), sg.InputText('', key='dia_semana')],
            [sg.Text('Telefone da Banda:', size=(15, 1)), sg.InputText('', key='telefone')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Bar Manager').Layout(layout)

        button, values = self.open()
        telefone = values['telefone']
        dia_semana = values['dia_semana']

        self.close()
        return {"dia_semana": dia_semana, "telefone": telefone}
    
    def mostra_agenda(self, dados_agenda):
        string_todos_agendas = ""
        for dado in dados_agenda:
            string_todos_agendas = string_todos_agendas + "DIA DA SEMANA: " + dado["dia_semana"] + '\n'
            string_todos_agendas = string_todos_agendas + "BANDA: " + dado["nome_banda"] + '\n\n'


        sg.Popup('-------- AGENDA SEMANAL ----------', string_todos_agendas)

    def seleciona_agenda(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- SELECIONAR DIA DA SEMANA DA AGENDA ----------', font=("Helvica", 25))],
            [sg.Text('Digite o dia da semana:', font=("Helvica", 15))],
            [sg.Text('DIA SEMANA:', size=(15, 1)), sg.InputText('', key='dia_semana')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona agenda').Layout(layout)

        button, values = self.open()
        dia_semana = values['dia_semana']
        self.close()
        return dia_semana

        





    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values