
class TelaCliente():
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def tela_opcoes(self):
    print("-------- CLIENTES ----------")
    print("Escolha a opcao")
    print("1 - Incluir Cliente")
    print("2 - Alterar Cliente")
    print("3 - Listar Clientes")
    print("4 - Excluir Cliente")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def pega_dados_cliente(self):
    print("-------- DADOS CLIENTE ----------")
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    cpf = input("CPF: ")

    return {"nome": nome, "telefone": telefone, "cpf": cpf}

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_cliente(self, dados_cliente):
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