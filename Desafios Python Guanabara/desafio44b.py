print('{:=^40}'.format(' LOJAS CÉSAR '))
valor = float(input('Valor da compra:R$ '))
print('''FORMAS DE PAGAMETO
[ 1 ] à vista no dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = valor - (valor * 10 / 100)
elif opcao == 2:
    total = valor - (valor * 5 / 100)
elif opcao == 3:
    total = valor
    parcela = total / 2
    print('Sua compra será parcelada em 2x de {:.2f}.'.format(parcela))
elif opcao == 4:
    total = valor + (valor * 20 / 100)
    totalParcelas = float(input('Quantas parcelas? '))
    parcela = total / totalParcelas
    print('Sua compra será parcela em {:.0f}x de R${:.2f} COM JUROS.'.format(totalParcelas, parcela))
else:
    total = valor
    print('Opção Inválida de Pagamento, tente novamente!!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor, total))
