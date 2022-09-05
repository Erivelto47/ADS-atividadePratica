print("Bem Vindo ao Controle de Estoque da Mercearia do Erivelto Sauzen Muller")

cod_produto_contador = 0
produtos = []


def cadastrar_produto(codigo_produto):
    print("Código do Produto {}".format(codigo_produto))
    nome_produto = input("Por favor entre com o NOME do Produto: ")
    fabricante = input("Por favor entre com o FABRICANTE do Produto:")
    valor = float(input("Por favor entre com o VALOR(R$) do Produto:"))
    produto_def = {
        'nome': nome_produto,
        'codigo': codigo_produto,
        'fabricante': fabricante,
        'valor': valor
    }

    produtos.append(produto_def.copy())


def consultar_produto():
    while True:
        opcao = int(input("Escolha a opcao desejada:\n"
                          '1- Consultar Todos os Produtos\n'
                          '2- Consultar Produtos por Código\n'
                          '3- Consultar Produtos por Fabricante\n'
                          '4- Retornar\n'))

        if opcao == 1:
            print("---------------------------------")
            for produto in produtos:
                for key, value in produto.items():
                    print("{} : {}".format(key, value))
            print("---------------------------------")

        elif opcao == 2:
            codigo = int(input("Digite o CODIGO do Produto: "))
            for produto in produtos:
                if produto['codigo'] == codigo:
                    for key, value in produto.items():
                        print("{} : {}".format(key, value))

        elif opcao == 3:
            fabricante = input("Digite o Fabricante do Produto: ")
            for produto in produtos:
                if produto['fabricante'] == fabricante:
                    for key, value in produto.items():
                        print("{} : {}".format(key, value))

        elif opcao == 4:
            break


def remover_produto():
    codigo = int(input("Digite o CODIGO do Produto a ser removido: "))
    for produto in produtos:
        if produto['codigo'] == codigo:
            produtos.remove(produto)


while True:
    opcao = int(input("Escolha a opcao desejada:\n"
                      '1- Cadastrar Produto\n'
                      '2- Consultar Produto(s)\n'
                      '3- Remover Produto\n'
                      '4- Sair\n'))

    if opcao == 1:
        print("Voce escolheu cadastrar um produto")
        cod_produto_contador += 1
        cadastrar_produto(cod_produto_contador)
    elif opcao == 2:
        print("Voce selecionou a Opcao de Consultar Produto")
        consultar_produto()
    elif opcao == 3:
        print("Voce selecionou a Opcao de Remover Produto")
        remover_produto()
    else:
        break