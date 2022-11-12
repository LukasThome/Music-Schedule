
class TelaCliente():
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
        print("-------- CLIENTES ----------")
        print("Escolha a opcao")
        print("1 - Incluir Cliente")
        print("2 - Alterar Cliente")
        print("3 - Listar Clientes")
        print("4 - Excluir Cliente")
        print("0 - Retornar")

        opcao = self.le_num_inteiro("Escolha a opcao:", [0, 1, 2, 3, 4])

        return opcao

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def pega_dados_cliente(self):
        print("\n")
        print("-------- DADOS CLIENTE ----------")
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        cpf = input("CPF: ")

        print("Cadsatro efetuado com sucesso!")
        print("\n")

        return {"nome": nome, "telefone": telefone, "cpf": cpf}

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado

    def mostra_cliente(self, dados_cliente):
        print("\n")
        print("NOME DO CLIENTE: ", dados_cliente["nome"])
        print("FONE DO CLIENTE: ", dados_cliente["telefone"])
        print("CPF DO CLIENTE: ", dados_cliente["cpf"])
        print("\n")

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def seleciona_cliente(self):
        cpf = input("CPF do cliente que deseja selecionar: ")
        return cpf

    def mostra_mensagem(self, msg):
        print(msg)
