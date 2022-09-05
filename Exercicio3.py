print("Bem vindo ao Programa de Feijoada do Erivelto Sauzen Muller")
print("Menu Volume Feijoada")


def volume_feijoada():
    volume = 0  # inicializa a variavel a ser retornada
    while True:
        try:  # trata a excecao se o usuário digitar um  uma letra por exemplo
            volume = int(input("Entre com a quantidade que deseja(ml): "))

            if 300 <= volume <= 5000:
                volume = volume * 0.08
                break
            else:
                print("Nao aceitamos porcoes menores que 300ml ou maiores que 5l. Tente novamente!")

        except ValueError:
            print("Digite um numero válido")
            continue
    return volume


def opcao_feijoada():
    multiplicador = 0  # inicializa a variavel a ser retornada
    while True:
        print("Menu opcao Feijoada")
        opcao_feijoada = input('Entre com a opcao de Feijoada: \n'
                               'b- Básica (Feijao + paiol + costelinha) \n'
                               'p- Premium (Feijao + paiol + costelinha + partes do porco) \n'
                               's- Suprema (Feijao + paiol + costelinha + partes do porco + charque + calabresa + bacon) \n '
                               '>>').upper()
        if opcao_feijoada != 'B' and opcao_feijoada != 'P' and opcao_feijoada != 'S':  # Verifica se a opcao digitada é aceitavel
            print("Você nao digitou uma opcao valida")
            continue

        if opcao_feijoada == 'B':
            multiplicador = 1
            break
        elif opcao_feijoada == 'P':
            multiplicador = 1.25
            break
        else:
            multiplicador = 1.5
            break

    return multiplicador


def acompanhamento_feijoada():
    total_acompanhamento = 0  # inicializa a variavel a ser retornada
    while True:
        try:  # trata a excessao da entrada do usuário
            opcao_acompanhamento = int(
                input('Deseja mais algum acompanhamento: \n'
                      '0- não desejo mais acompanhamentos (encerrar pedido) \n'
                      '1- 200g de arroz \n'
                      '2- 150g de farofa especial \n'
                      '3- 100g de couve cozida \n'
                      '4- 1 laranja descascada \n'
                      '>>'))
            if opcao_acompanhamento == 1:
                total_acompanhamento += 5
            elif opcao_acompanhamento == 2:
                total_acompanhamento += 6
            elif opcao_acompanhamento == 3:
                total_acompanhamento += 7
            elif opcao_acompanhamento == 4:
                total_acompanhamento += 3
            elif opcao_acompanhamento == 0:
                break

        except ValueError:
            print("Opcao invalida.")
            continue
    return total_acompanhamento


volume = volume_feijoada()
opcao = opcao_feijoada()
adicionais = acompanhamento_feijoada()

total = (volume * opcao) + adicionais

print("O valor a ser pago é (R$): {:.2f} (volume = {} * opcao = {} + acompanhamento = {:.2f})"
      .format(total, volume, opcao, adicionais))
