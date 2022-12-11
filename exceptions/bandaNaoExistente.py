
class BandaNaoExistenteException(Exception):
    def __init__(self):
        self.mensagem = "Banda não existe"

        
        super().__init__(self.mensagem)
        