class AgendaListaVaziaException(Exception):
    def __init__(self):
        self.mensagem = "Agenda vazia!"

        
        super().__init__(self.mensagem)
        