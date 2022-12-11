class ClienteListaVaziaException(Exception):
    def __init__(self):
        self.mensagem = "Nenhum cliente cadastrado!"

        
        super().__init__(self.mensagem)
        