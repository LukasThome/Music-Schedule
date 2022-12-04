class TelaRelatorio():

    def le_num_inteiro(self, mensagem=" ", ints_validos=None):
        while True:
            valor_lido = input(mensagem)
            try:
                # tenta transformar o valor lido em inteiro.
                valor_int = int(valor_lido)
                if ints_validos and valor_int not in ints_validos:
                    raise ValueError  # será lançada apenas se o número não é o esperado
                return valor_int
            except ValueError:  # aqui cai se não for int ou se não for valido
                print("Valor incorreto!")
                if ints_validos:
                    print("Valores válidos: ", ints_validos)
    
    
    
    def tela_opcoes(self):
        print("\n")
        print("-------- RELATORIO----------")
        print("Escolha a opcao")
        print("1 - Criar Relatório")
        print("2 - Mostrar Relatório")
        print("3 - Deletar Relatório")
        print("0 - Retornar")

        opcao = self.le_num_inteiro("Escolha a opcao:", [0, 1, 2, 3])

        return opcao

    def pega_dados_relatorio(self):
        print("\n")
        dia_semana = input("Insira o dia da semana: ")
        return {"dia_semana": dia_semana}

    def mostra_relatorio(self, dados_relatorio):
        print("\n")
        print("DIA DA SEMANA: ", dados_relatorio["dia_semana"])
        print("NOME DA BANDA: ", dados_relatorio["nome_banda"])
        print("NÚMERO DE PESSOAS: ", dados_relatorio["numero_pessoas"])

    def mostra_mensagem(self, msg):
        print(msg)
