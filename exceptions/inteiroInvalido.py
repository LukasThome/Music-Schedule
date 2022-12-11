
class InteiroInvalidopException(Exception):
    def __init__(self):
        self.mensagem = "Insira um numero inteiro"

        
        super().__init__(self.mensagem)
        