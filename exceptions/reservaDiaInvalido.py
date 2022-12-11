class ReservaDiaInvalidoException(Exception):
    def __init__(self):
        self.mensagem = "Dia da Semana inválido! Tente SEG TER QUA QUI SEX SAB ou DOM"

        
        super().__init__(self.mensagem)
        