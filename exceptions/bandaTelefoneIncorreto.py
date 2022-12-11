
class BandaTelefoneIncorretoException(Exception):
    def __init__(self):
        self.mensagem = "Telefone Incorreto ou inexistente"

        
        super().__init__(self.mensagem)
        