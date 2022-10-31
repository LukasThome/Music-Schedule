class TelaReserva():
    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def tela_opcoes(self):
        print("\n")
        print("-------- RESERVAS ----------")
        print("Escolha a opcao")
        print("1 - Fazer Reserva")
        print("2 - Listar Reservas")
        print("3 - Cancelar Reserva")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))

        return opcao

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def pega_dados_reserva(self):
        print("\n")
        print("-------- DADOS RESERVA ----------")
        dia_semana = input("Insira o dia da semana: ")
        cpf = input("Insira seu CPF: ")
        numero_pessoas = input("Número de Pessoas: ")
        print("Reserva efetuada com sucesso!")
        print("Aguardamos vocês!")

        return {"dia_semana": dia_semana, "cpf": cpf, "numero_pessoas": numero_pessoas}

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def mostra_reserva(self, dados_reserva):
        print("\n")
        print("CODIGO DO RESERVA: ", dados_reserva["codigo"])
        print("DIA DA SEMANA: ", dados_reserva["dia_semana"])
        print("NOME DO CLIENTE ", dados_reserva["nome_cliente"])
        print("CPF DO CLIENTE: ", dados_reserva["cpf_cliente"])
        print("NÚMERO DE PESSOAS ", dados_reserva["numero_pessoas"])

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def seleciona_reserva(self):
        codigo = input("Código do reserva que deseja selecionar: ")
        print("\n")
        return codigo

    def mostra_mensagem(self, msg):
        print(msg)
