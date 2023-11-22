from math import ceil
print('\033[1;31mO Financiamento de uma CASA.\033[m\n')

valorCasa = float(input('Qual o valor da casa que você deseja financiar: R$ '))
print('Valor do Imóvel: R${:.3f}\n'.format(valorCasa))
salario = float(input('Informe o seu salário: R$ '))
print('Salário atual R${:.2f}\n'.format(salario))
prazo = int(input('Em quantos meses você pretende financiar? '))

prestacao = valorCasa / prazo
limite = salario * 30 / 100
print('Seu limite para prestação é de R${:.2f}.\n'.format(limite))

if prestacao >= limite:
    print('A prestação fica no total de R${:.2f} e excede o seu limite de R${:.2f} que é de 30% do seu salário, o financiamento não será possível. Desculpe!'.format(prestacao, limite))
elif prestacao <= limite:
    print('Empréstimo CONCEDIDO!!\n A prestação mensal do seu financiamento será de R${:.2f}.PARABÉÉÉNS!!!'.format(prestacao))

print('---FIM!!---')