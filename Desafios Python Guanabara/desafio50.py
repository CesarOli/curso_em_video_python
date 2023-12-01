print('\033[1;31mSomando os números Pares.\033[m\n')
print('\033[33mVoce vai precisar informar seis números inteiros.\n\033[m')
soma = 0
for c in range(1, 7):
    numeros = int(input('Informe um número inteiro: '))
    if numeros % 2 == 0:
        soma = soma + numeros
print('\033[7;37m Você informou {} números. E a soma dos números pares é igual a {}.\033[m'.format(c, soma))
