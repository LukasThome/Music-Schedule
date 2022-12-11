class ReservaListaVaziaException(Exception):
    def __init__(self):
        self.mensagem = "Nenhuma reserva cadastrada!"

        
        super().__init__(self.mensagem)
        