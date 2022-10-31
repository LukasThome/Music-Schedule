class TelaRelatorio():

    def tela_opcoes(self):
        print("\n")
        print("-------- RELATORIO----------")
        print("Escolha a opcao")
        print("1 - Criar Relatório")
        print("2 - Mostrar Relatório")
        print("3 - Deletar Relatório")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))

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
