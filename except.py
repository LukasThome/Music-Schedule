from jogo_duplicado_exception import JogoDuplicadoException


class JogoDuplicadoException(Exception):
    def __init__(self):
        super().__init__("O jogo já está cadastrado no sistema!")


        #Thaís Bardini Idalino7: 45 PM
        if self.busca_jogo_por_numero(jogo.numero) is not None:
                            #raise JogoDuplicadoException
            try:
                pass

            except JogoDuplicadoException:
                pass
            #self.__tela.mostramsg("Jogo repetido"


       
            self.__tela_amigo.mostra_mensagem(str(e))

        

    ##-- Professores: 

##Thais Bardini Idalino
##E-mail: thais.bardini@ufsc.br
##Atendimento: quartas-feiras das 13:00-15:00, sala 420. Enviar email para agendamento.
##
##Wyllian Bezerra da Silva
##Atendimento: quartas-feiras das 9:00-11:00, sala 410.