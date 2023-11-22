print('\033[1;31mComparando números.\n\033[m')

n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
if n1 > n2:
    print('O número {} é maior que {}.'.format(n1, n2))
elif n2 > n1:
    print('\nO número {} é maior que {}.'.format(n2, n1))
else:
    print('\nOs números são iguais, tente novamente.')
print('\nFIM')