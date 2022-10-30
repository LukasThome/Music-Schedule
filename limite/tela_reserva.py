class TelaReserva():
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def tela_opcoes(self):
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
    print("-------- DADOS RESERVA ----------")
    cpf = input("CPF Cliente: ")
    numero_pessoas = input("Número de Pessoas: ")

    return {"cpf": cpf, "numero_pessoas": numero_pessoas}

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_reserva(self, dados_reserva):
    print("CODIGO DO RESERVA: ", dados_reserva["codigo"])
    print("NOME DO CLIENTE ", dados_reserva["nome_cliente"])
    print("CPF DO CLIENTE: ", dados_reserva["cpf_cliente"])
    print("NÚMERO DE PESSOAS ", dados_reserva["numero_pessoas"])
    print("\n")

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_reserva(self):
    codigo = input("Código do reserva que deseja selecionar: ")
    return codigo

  def mostra_mensagem(self, msg):
    print(msg)