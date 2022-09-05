print('Bem-Vindo a Pizzaria do Erivelto Sauzen Muller')
total = 0  # Inicializa o total a ser pago
print(
    '----------------------Cardápio---------------------- \n '
    '| Código | Descricão  | Pizza Média | Pizza Grande | \n '
    '|   21   | Napolitana |    R$ 20,00 |     R$ 26,00 | \n '
    '|   22   | Margherita |    R$ 20,00 |     R$ 26,00 | \n '
    '|   23   | Calabresa  |    R$ 25,00 |     R$ 32,50 | \n '
    '|   24   | Toscana    |    R$ 30,00 |     R$ 39,00 | \n '
    '|   25   | Portuguesa |    R$ 30,00 |     R$ 39,00 | \n '
    '---------------------------------------------------- \n '
)
while True:
    tamanho_pizza = input("Qual o tamanho de pizza que deseja (M/G): \n >> ").upper()

    if tamanho_pizza != 'M' and tamanho_pizza != 'G':
        print('Opção Inválida')
        continue  # Volta para o cadápio

    try:  # Tratativa de erro quando o usuário digitar um valor invalido
        codigo = int(input("Entre com o código do sabor desejado: \n >> "))

        if codigo == 21:
            print("Voce pediu uma Pizza Napolitana")
            if tamanho_pizza == 'M':
                total += 20
            else:
                total += 26
        elif codigo == 22:
            print("Voce pediu uma Pizza Margherita")
            if tamanho_pizza == 'M':
                total += 20
            else:
                total += 26
        elif codigo == 23:
            print("Voce pediu uma Pizza Calabresa")
            if tamanho_pizza == 'M':
                total += 25
            else:
                total += 32.50
        elif codigo == 24:
            print("Voce pediu uma Pizza Toscana")
            if tamanho_pizza == 'M':
                total += 30
            else:
                total += 39
        elif codigo == 25:
            print("Voce pediu uma Pizza Portuguesa")
            if tamanho_pizza == 'M':
                total += 30
            else:
                total += 39
        else:
            print("Opcao Inválida")
            continue
    except ValueError:
        print("Foi insirido um valor não numérico")
        continue  # volta para o começo do while
    resposta = int(input("Voce deseja pedir mais alguma coisa?\n 1 - Sim \n 0 - Não \n >> "))
    if resposta == 1:
        continue
    else:
        print("O total a ser pago é: " + "R$ {:.2f}".format(total))
        break
