class TelaSistema:

    # essa função trata o caso de não digitar um valor valido
    # note que está dentro de um while True. Só sai do loop quando digitado um valor correto
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
        print("-------- Bar do Python ---------")
        print("Escolha sua opcao")
        print("1 - Bandas")
        print("2 - Clientes")
        print("3 - Reservas")
        print("4 - Agenda Musical")
        print("5 - Relatório")
        print("0 - Finalizar sistema")
        opcao = self.le_num_inteiro("Escolha a opcao:", [0, 1, 2, 3, 4, 5])
        print("\n")
        return opcao
