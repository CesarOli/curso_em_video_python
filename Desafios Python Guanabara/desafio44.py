from math import ceil
print('\033[1;31mGerenciando Pagamentos.\033[m\n')
print('\033[1;33m=====LOJAS CÉSAR=====\033[m\n')
valorTotalCompra = float(input('Qual o valor total da compra? R$ '))
print('O valor total da sua compra foi {:.2f}.'.format(valorTotalCompra))
print('''Como você gostaria de realizar o pagamento?
[ 1 ] à vista no dinheiro/cheque.
[ 2 ] à vista no cartao.
[ 3 ] em até 2x no cartão.
[ 4 ] 3x ou mais no cartão.''')
opcao = int(input('Qual a sua opçao de pagamento? '))
if opcao == 1:
    desconto = valorTotalCompra * 10 / 100
    novoValor = valorTotalCompra - desconto
    print('Voce teve um desconto de 10% pela forma de pagamento, o novo valor total a pagar'
          ' é de R${:.2f}, obrigado!!'.format(novoValor))
elif opcao == 2:
    desconto = valorTotalCompra * 5 / 100
    novoValor = valorTotalCompra - desconto
    print('Você teve um desconto de 5% pela forma de pagamento, o novo valor total a pagar'
          ' é de R${}.'.format(novoValor))
elif opcao == 3:
    novoValor = valorTotalCompra
    parcelas = novoValor / 2
    print('Você pagará o valor total de R${:.2f}, em até 2x de {:.2f} no cartão de crédito, sem a cobrança juros.'.format(valorTotalCompra, parcelas))
elif opcao == 4:
    parcelas = int(input('Em quantas parcelas: '))
    juros = valorTotalCompra * 20 / 100
    novoValor = valorTotalCompra + juros
    parcelado = novoValor / parcelas
    print('Para esta opção de pagamento, o valor total da compra será de R${:.2f},'.format(novoValor))
    print('em {}x de R${:.2f}.'.format(parcelas, parcelado), 'no cartão de crédito. Este valor, pois houve a cobrança de 20% de juros.')
else:
    total = valorTotalCompra
    print('Opção inválida de pagamento, tente novamente.')
    print('Sua compra vai custar {:.2f}, no final'. format(valorTotalCompra))