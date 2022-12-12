class BandaListaVaziaException(Exception):
    def __init__(self):
        self.mensagem = "Nenhuma banda cadastrada!"

        
        super().__init__(self.mensagem)
        