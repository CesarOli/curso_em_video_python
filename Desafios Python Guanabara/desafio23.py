'''print('Separado por Unidade, Dezena, Centena e Milhar utilizando "str".')
numero = int(input('Informe um número de 0 a 9999: '))
num = str(numero)
print('Analisando o número digitado {}, temos:'.format(num))
print('Unidade: {}'.format(num[3]))
print('Dezena: {}'.format(num[2]))
print('Centena: {}'.format(num[1]))
print('Milhar: {}'.format(num[0]))
print('\nObrigado!!')'''

print('\nResolvendo matematicamente\n')
numero = int(input('Informe um número de 0 a 9999: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))
print('\nObrigado!!')