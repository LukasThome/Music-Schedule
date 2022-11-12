class TelaBanda():
    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
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
        print("-------- BANDAS ----------")
        print("Escolha a opcao")
        print("1 - Incluir Banda")
        print("2 - Alterar Banda")
        print("3 - Listar Banda")
        print("4 - Excluir Banda")
        print("0 - Retornar")

        opcao = self.le_num_inteiro("Escolha a opcao:", [0, 1, 2, 3, 4])

        return opcao

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def pega_dados_banda(self):
        print("\n")
        print("-------- DADOS BANDA ----------")
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        estilo = input("Estilo musical da banda: ")

        return {"nome": nome, "telefone": telefone, "estilo": estilo}

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def mostra_banda(self, dados_banda):
        print("\n")
        print("NOME DA BANDA: ", dados_banda["nome"])
        print("TELEFONE DO BANDA: ", dados_banda["telefone"])
        print("ESTILO MUSICAL DA BANDA: ", dados_banda["estilo"])

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado

    def seleciona_banda(self):
        telefone = input("Telefone do banda que deseja selecionar: ")
        return telefone

    def mostra_mensagem(self, msg):
        print(msg)
