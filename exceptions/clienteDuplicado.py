
class ClienteDuplicadaException(Exception):
    def __init__(self):
        self.mensagem = "Cliente já existente"

        
        super().__init__(self.mensagem)
        