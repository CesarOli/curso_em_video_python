print('\033[31mO CONVERSOR!\033[m')

numero = int(input('Informe um número: '))
print('''Escolha a base de conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL\n''')
escolha = int(input('Sua escolha: '))
if escolha == 1:
    print('O número {} em BINÁRIO é {}.'.format(numero, bin(numero)[2:]))
elif escolha == 2:
    print('O número {} em Octal é {}.'.format(numero, oct(numero)[2:]))
elif escolha == 3:
    print('O número {} em HEXADECIMAL é {}.'.format(numero, hex(numero)[2:]))
else:
    print('Escolha um número entre 1 e 3. Obrigado!!')
print('\nFIM.')