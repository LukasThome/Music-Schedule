
class BandaDuplicadaException(Exception):
    def __init__(self):
        self.mensagem = "Banda já existente"

        
        super().__init__(self.mensagem)
        