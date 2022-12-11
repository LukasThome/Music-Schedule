
class ReservaNaoExistenteException(Exception):
    def __init__(self):
        self.mensagem = "Reserva não existe"

        
        super().__init__(self.mensagem)
        