
class RelatorioListaVaziaException(Exception):
    def __init__(self):
        self.mensagem = "Nenhum relatório gerado para ser exibido"

        
        super().__init__(self.mensagem)
        