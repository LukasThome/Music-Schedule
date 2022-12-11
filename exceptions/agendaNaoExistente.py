
class AgendaNaoExistenteException(Exception):
    def __init__(self):
        self.mensagem = "Agenda não existe"

        
        super().__init__(self.mensagem)
        