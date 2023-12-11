print('\033[1;31mMaior e Menor valores.\033[m\n')
n1 = int(input('Informe um número inteiro: '))
resposta = str(input('Deseja continuar, [S/N]: ')).upper()
media = soma = count = 0
while resposta == 'S':
    if resposta == 'S':
        n = int(input('Informe um novo número: '))
        soma = soma + n1 + n
        resposta = str(input('Deseja continuar, [S/N]: ')).upper()
    else:
        print('Por favor, digite somente "S" para SIM, "N" para NÃO, obrigado!')
print(soma)
