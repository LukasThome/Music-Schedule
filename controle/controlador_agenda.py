from entidade.agenda import Agenda
from limite.tela_agenda import TelaAgenda


class ControladorAgenda():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        #self.__agenda = {'TE': '', 'QA': '',
            #'QI': '', 'SE': '', 'SA': '', 'DO': ''}
        self.__agendas = []
        self.__tela_agenda = TelaAgenda()

    def incluir_banda_agenda(self):
        # vai fazer um print das bandas cadastradas
        self.__controlador_sistema.controlador_bandas.lista_banda()
        # vai chamr o metodo da tela agenda para ler os valores
        dados_agenda = self.__tela_agenda.pega_dados_agenda()

        # pega banda por telefone
        banda = self.__controlador_sistema.controlador_bandas.pega_banda_por_telefone(dados_agenda["telefone"])
        dia_semana = dados_agenda["dia_semana"]
    

        # instancia o objeto agenda
        agenda = Agenda(banda,  dia_semana)
        # existe uma lista de agendas
        self.__agendas.append(agenda)

        # metodo para incluir a banda no dicionadrio banda
        
        
        #self.__agenda.update({dia_semana, 'Sirigaita'})

    def mostra_agenda(self):
        for r in self.__agendas:
            #chama o metodo da tela_agenda
            self.__tela_agenda.mostra_agenda({"dia_semana": r.dia_semana,
                                                "nome_banda": r.banda.nome,
                                                })

        
        

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_banda_agenda, 2: self.mostra_agenda, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_agenda.tela_opcoes()]()