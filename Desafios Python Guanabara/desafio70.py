print('\033[1;31mEstatísticas em produtos\033[m')
totalGasto = maior1000 = menorValor = 0
produtoMenorValor = ' '
while True:
    produto = str(input('Digite o produto que você comprou: '))
    valorProduto = float(input(('Digite o valor deste produto: ')))
    resposta = ' '
    totalGasto += valorProduto
    if valorProduto >= 1000:
        maior1000 += 1
    if valorProduto < menorValor:
        menorValor = valorProduto
        produtoMenorValor = produto
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if resposta == 'N':
        break
print(f'O total da compra é de R${totalGasto} reais.')
print(f'{maior1000} produtos da sua lista custam mais que R$1000,00.')
print(f'O produto de menor valor é o {produtoMenorValor}.')
print('Obrigado pela compra!!\n')
print('FIM')

