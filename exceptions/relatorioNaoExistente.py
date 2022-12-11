
class RelatorioNaoExistenteException(Exception):
    def __init__(self):
        self.mensagem = "Relatorio não existe"

        
        super().__init__(self.mensagem)
        