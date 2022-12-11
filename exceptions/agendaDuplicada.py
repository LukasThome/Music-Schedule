
class AgendaDuplicadaException(Exception):
    def __init__(self):
        self.mensagem = "Já temos atração musical neste dia"

        
        super().__init__(self.mensagem)
        