print('\033[1;31mVários Números com Flags.\033[m')
cont = s = n = 0
while True:
    n = int(input('Digite um número, [999 para sair do programa]: '))
    if n == 999:
        break
    s = s + n
    cont += 1
print(f'A soma entre os números digitados é de {s}, e quantidade de números digitados foi de {cont}.')
print('Fim do Programa.')
