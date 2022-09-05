print('Bem vindo a loja do Erivelto Sauzen Muller')
total_desconto = 0  # cria a variavel total com desonto, setando com valor zero
total = 0  # cria a variavel total, neste caso sem desconto, com valor zero
try:    # Adicionado try para evitar erros do usuário ao digitar
    valor = float(input('Entre com o valor do produto: \n'))
    quantidade = int(input('Entre com valor da quantidade: \n'))

    if quantidade <= 4:
        total = valor * quantidade
    elif 5 <= quantidade <= 19:
        desconto = "(desconto 3%)"
        total = (valor * quantidade)
        total_desconto = total * 0.97
    elif 20 <= quantidade <= 99:
        desconto = "(desconto 6%)"
        total = (valor * quantidade)
        total_desconto = total * 0.94
    elif quantidade >= 100:
        desconto = "(desconto 10%)"
        total = (valor * quantidade)
        total_desconto = total * 0.9

    print('O valor sem desconto foi: ' + 'R$ {:.2f}'.format(total))
    if total_desconto > 0:  # Verifica se existe um total com desconto
        print('O valor com desconto foi: ' + 'R$ {:.2f}'.format(total_desconto) + ' ' + desconto)

except ValueError:
    print("Foi insirido um valor não numérico")
