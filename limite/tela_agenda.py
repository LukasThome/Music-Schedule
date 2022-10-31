class TelaAgenda():

    def tela_opcoes(self):
        print("\n")
        print("-------- AGENDA MUSICAL ----------")
        print("Escolha a opcao")
        print("1 - Criar Agenda")
        print("2 - Mostra Agenda")
        #print("3 - Excluir Agenda")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))

        return opcao

    def pega_dados_agenda(self):
        print("\n")
        print("-------- DADOS AGENDA MUSICAL ----------")
        dia_semana = input("Dia da semana: ")
        telefone = input("Telefone da Banda: ")

        # usaremos estes dados no controller
        return {"dia_semana": dia_semana, "telefone": telefone}

    def mostra_agenda(self, dados_agenda):

        print(dados_agenda["dia_semana"], ":", dados_agenda["nome_banda"])

    # def seleciona_agenda(self):
    #codigo = input("Código da agenda que deseja selecionar: ")
    # return codigo

    def mostra_mensagem(self, msg):
        print(msg)
