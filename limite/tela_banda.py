class TelaBanda():
    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def tela_opcoes(self):
        print("\n")
        print("-------- BANDAS ----------")
        print("Escolha a opcao")
        print("1 - Incluir Banda")
        print("2 - Alterar Banda")
        print("3 - Listar Banda")
        print("4 - Excluir Banda")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))

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
