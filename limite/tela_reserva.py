class TelaReserva():
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def tela_opcoes(self):
    print("-------- RESERVAS ----------")
    print("Escolha a opcao")
    print("1 - Fazer Reserva")
    print("2 - Listar Reservas")
    print("3 - Devolver Reserva")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def pega_dados_reserva(self):
    print("-------- DADOS RESERVA ----------")
    cpf = input("CPF Cliente ")
    telefone = input("Telefone Banda: ")

    return {"cpf": cpf, "telefone": telefone}

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_reserva(self, dados_reserva):
    print("CODIGO DO RESERVA: ", dados_reserva["telefone"])
    print("NOME DA BANDA: ", dados_reserva["nome_banda"])
    print("TELEFONE DA BANDA: ", dados_reserva["telefone_banda"])
    print("NOME DO CLIENTE ", dados_reserva["nome_cliente"])
    print("CPF DO CLIENTE: ", dados_reserva["cpf_cliente"])
    print("\n")

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_reserva(self):
    codigo = input("Código do reserva que deseja selecionar: ")
    return codigo

  def mostra_mensagem(self, msg):
    print(msg)