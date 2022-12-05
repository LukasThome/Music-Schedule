from entidade.agenda import Agenda
from limite.tela_agenda import TelaAgenda


class ControladorAgenda():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        
        ###agendas pre-definidas para teste###
        banda = self.__controlador_sistema.controlador_bandas.pega_banda_por_telefone("112")
        agenda01 = Agenda(banda, "TER")
        banda = self.__controlador_sistema.controlador_bandas.pega_banda_por_telefone("113")
        agenda02 = Agenda(banda, "QUAR")
        banda = self.__controlador_sistema.controlador_bandas.pega_banda_por_telefone("114")
        agenda03 = Agenda(banda, "QUI")
        ### ----- ###
        
        
        self.__agendas = [agenda01, agenda02, agenda03]
        self.__tela_agenda = TelaAgenda()

        

    def pega_banda_por_dia_semana(self, dia_semana):
        for agenda in self.__agendas:
            if (agenda.dia_semana == dia_semana):
                return agenda.banda
        return None

    def incluir_banda_agenda(self):
        # vai fazer um print das bandas cadastradas
        self.__controlador_sistema.controlador_bandas.lista_banda()
        # vai chamr o metodo da tela agenda para ler os valores
        dados_agenda = self.__tela_agenda.pega_dados_agenda()

        # pega banda por telefone
        banda = self.__controlador_sistema.controlador_bandas.pega_banda_por_telefone(
            dados_agenda["telefone"])
        dia_semana = dados_agenda["dia_semana"]

        

        # instancia o objeto agenda
        agenda = Agenda(banda,  dia_semana)
        # Adiciona a uma lista de agendas
        self.__agendas.append(agenda)

    def lista_agenda(self):
        if len(self.__agendas) == 0:
            #Adicionar a classe de exception aqui
            print("\n")
            print("Lista de agendas vazia")
        else:
            dados_agendas = []
            for agenda in self.__agendas:
                #self.__tela_agenda.mostra_agenda({"nome": agenda.nome, "telefone": agenda.telefone, "cpf": agenda.cpf})
                dados_agendas.append({"dia_semana": agenda.dia_semana, "nome_banda": agenda.banda.nome})
            self.__tela_agenda.mostra_agenda(dados_agendas)

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_banda_agenda,
                        2: self.lista_agenda, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_agenda.tela_opcoes()]()
