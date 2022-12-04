class TelaAgenda():

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
        print("-------- AGENDA MUSICAL ----------")
        print("Escolha a opcao")
        print("1 - Criar Agenda")
        print("2 - Mostra Agenda")
        #print("3 - Excluir Agenda")
        print("0 - Retornar")

        opcao = self.le_num_inteiro("Escolha a opcao:", [0, 1, 2, 3])

        return opcao

    def pega_dados_agenda(self):
        print("\n")
        print("-------- DADOS AGENDA MUSICAL ---------")
        dia_semana = input("Dia da semana: ")
        telefone = input("Telefone da Banda: ")

        # usaremos estes dados no controller
        return {"dia_semana": dia_semana, "telefone": telefone}

    def mostra_agenda(self, dados_agenda):

        print(dados_agenda["dia_semana"], ":", dados_agenda["nome_banda"])

    def mostra_mensagem(self, msg):
        print(msg)
