
class OpcaoInvalidaException(Exception):
    def __init__(self):
        self.mensagem = "Selecione uma opcão!"

        
        super().__init__(self.mensagem)
        