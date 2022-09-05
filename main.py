# --------------------------------EXEMPLO--------------------------------
print('Programa de Agendamento de Banho do Renan Portela Jorge')
total = 0  # Recebe o valor total a ser pago pelo cliente
contador = 0  # conta a quantidade de cachorros
while True:
    pelo = input('Qual o tipo de pelo do seu cachorro?\n '
                 'C - Curto\n '
                 'M - Médio\n '
                 'L - Longo\n'
                 '>>')
    if pelo == 'C':
        subtotal = 20
    elif pelo == 'M':
        subtotal = 25
    elif pelo == 'L':
        subtotal = 30
    else:
        print('Opção Inválida')
        continue  # volta para o começo do while
    try:  # Try para evitar erro quando o usuário digitar um valor não numérico
        peso = int(input('Quantos quilogramas tem o seu cachorro?\n'
                         '>>'))
        if 0 <= peso < 5:
            subtotal *= 1.8
        elif 5 <= peso < 12:
            subtotal *= 2.0
        elif 12 <= peso < 22:
            subtotal *= 2.4
        elif 22 <= peso < 35:
            subtotal *= 2.8
        elif 35 <= peso < 50:
            subtotal *= 3.4
        else:
            subtotal *= 4
    except ValueError:
        print("Foi insirido um valor não numérico")
        continue  # volta para o começo do while
    nome_cao = input('Digite o nome do cachorro:')
    print("O Banho do " + nome_cao + " ficou: " + " R$ {:.2f}".format(subtotal))
    contador = contador + 1
    total = total + subtotal  # somatório de subtotais
    resposta = input('Deseja dar banho em mais algum cachorro?\n'
                     'Digite (S) para continuar...\n'
                     'Ou pressione qualquer tecla para fechar a conta...\n'
                     '>>')
    if resposta.upper() == 'S':
        continue
    else:
        # valor de desconto de 10% para cada cachorro
        desconto = (total * 0.1) * (contador - 1)
        total = total - desconto
        print("O Total do(s) {} cachorro(s) ficou:\n" "R${:.2f} (desconto de R${:.2f})".format(contador, total,
                                                                                               desconto))
        break
