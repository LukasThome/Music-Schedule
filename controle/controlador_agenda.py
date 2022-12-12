from entidade.agenda import Agenda
from limite.tela_agenda import TelaAgenda
from exceptions.agendaListaVazia import AgendaListaVaziaException
from exceptions.agendaNaoExistente import AgendaNaoExistenteException
from exceptions.reservaDiaInvalido import ReservaDiaInvalidoException
from exceptions.bandaTelefoneIncorreto import BandaTelefoneIncorretoException
from exceptions.agendaDuplicada import AgendaDuplicadaException
from DAOs.agenda_dao import AgendaDAO

class ControladorAgenda():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__agenda_DAO = AgendaDAO()
        ### agendas pre-definidas para teste###
        #banda = self.__controlador_sistema.controlador_bandas.pega_banda_por_telefone(
        #    "112")
        #agenda01 = Agenda(banda, "TER")
        #banda = self.__controlador_sistema.controlador_bandas.pega_banda_por_telefone(
        #    "113")
        #agenda02 = Agenda(banda, "QUA")
        #banda = self.__controlador_sistema.controlador_bandas.pega_banda_por_telefone(
         #   "114")
        #agenda03 = Agenda(banda, "QUI")
        ### ----- ###

        #self.__agendas = [agenda01, agenda02, agenda03]
        self.__tela_agenda = TelaAgenda()

    # pegar a banda por dia da semana e retorna a banda

    def pega_banda_por_dia_semana(self, dia_semana: str):
        for agenda in self.__agenda_DAO.get_all():
            if (agenda.dia_semana == dia_semana):
                return agenda.banda
        return None

    def incluir_banda_agenda(self):
        telefone_valido = bool
        repetido = bool
        dia_valido = bool
        
        # vai fazer um print das bandas cadastradas
        self.__controlador_sistema.controlador_bandas.lista_banda()
        # vai chamr o metodo da tela agenda para ler os valores
        dados_agenda = self.__tela_agenda.pega_dados_agenda()

        # pega banda por telefone
        banda = self.__controlador_sistema.controlador_bandas.pega_banda_por_telefone(
            dados_agenda["telefone"])
        try:
            if banda is None:
                telefone_valido = False
                raise BandaTelefoneIncorretoException
            else:
                telefone_valido = True
        except BandaTelefoneIncorretoException as e:
            self.__tela_agenda.mostra_mensagem(e)

        dia_semana = dados_agenda["dia_semana"]
        dias_validos = ["SEG", "TER", "QUA", "QUI", "SEX", "SAB", "DOM"]

        telefone_valido = bool
        repetido = bool
        dia_valido = bool
        
        
        try:
            for agenda in self.__agenda_DAO.get_all():
                if agenda.dia_semana != dia_semana:
                    repetido = False
                else:
                    repetido = True
                    raise AgendaDuplicadaException
                    
        except AgendaDuplicadaException as e:
            self.__tela_agenda.mostra_mensagem(e)
            
        
        try:
            if dia_semana in dias_validos:
                dia_valido = True
            else:
                dia_valido = False
                raise ReservaDiaInvalidoException
        except ReservaDiaInvalidoException as e:
            self.__tela_agenda.mostra_mensagem(e)

        if dia_valido == True and repetido == False and telefone_valido == True:
            # instancia o objeto agenda
                agenda = Agenda(banda,  dia_semana)
                # Adiciona a uma lista de agendas
                self.__agenda_DAO.add(agenda)
                #self.__agendas.append(agenda)

    def lista_agenda(self):
        try:
            if len(self.__agenda_DAO.get_all()) != 0:
                dados_agendas = []
                for agenda in self.__agenda_DAO.get_all():
                    #self.__tela_agenda.mostra_agenda({"nome": agenda.nome, "telefone": agenda.telefone, "cpf": agenda.cpf})
                    dados_agendas.append(
                        {"dia_semana": agenda.dia_semana, "nome_banda": agenda.banda.nome})
                self.__tela_agenda.mostra_agenda(dados_agendas)
            else:
                raise AgendaListaVaziaException

        except AgendaListaVaziaException as e:
            self.__tela_agenda.mostra_mensagem(e)

    def pega_agenda_por_dia_semana(self, dia_semana: str):
        for agenda in self.__agenda_DAO.get_all():
            if (agenda.dia_semana == dia_semana):
                return agenda
        return None

    def excluir_banda_agenda(self):
        self.lista_agenda()
        #dia_semana = self.__tela_agenda.seleciona_agenda()
        #agenda = self.pega_banda_por_dia_semana(dia_semana)

        dia_semana = self.__tela_agenda.seleciona_agenda()

        agenda = self.pega_agenda_por_dia_semana(dia_semana)

        dias_validos = ["SEG", "TER", "QUA", "QUI", "SEX", "SAB", "DOM"]
        try:
            if dia_semana not in dias_validos:
                raise ReservaDiaInvalidoException
        except ReservaDiaInvalidoException as e:
            self.__tela_agenda.mostra_mensagem(e)

        try:
            if (agenda is not None):
                self.__agenda_DAO.remove(agenda.dia_semana)
                #self.__agendas.remove(agenda)
                self.lista_agenda()
            else:
                raise AgendaNaoExistenteException
        except AgendaNaoExistenteException as e:
            self.__tela_agenda.mostra_mensagem(e)

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_banda_agenda,
                        2: self.lista_agenda, 3: self.excluir_banda_agenda, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_agenda.tela_opcoes()]()
