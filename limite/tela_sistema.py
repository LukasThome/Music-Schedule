import PySimpleGUI as sg

class TelaSistema:

    def __init__(self):
        self.__window = None
        self.init_components()


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

    def mostra_mensagem(self, msg):
        sg.popup("", msg)