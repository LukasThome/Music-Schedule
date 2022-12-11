class ClienteNaoExistenteException(Exception):
    def __init__(self):
        self.mensagem = "Cliente não existente"

        
        super().__init__(self.mensagem)
        