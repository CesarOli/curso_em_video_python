from time import sleep
print('\033[1;31mCriando Menu de Opções.\033[m')
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opcao = soma = multi = maior = 0
while opcao != 5:
    print('''\033[1;33m 
[1] somar
[2] multiplicação
[3] maior
[4] novos números
[5] sair do programa\033[m''')
    opcao = int(input('Diga qual é sua opção: '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é igual a {}.'.format(n1, n2, soma))
    elif opcao == 2:
        multi = n1 * n2
        print('A multiplicação entre {} e {} é {}.'.format(n1, n2, multi))
    elif opcao == 3: #usando o ELIF, quando coloco a opção 3 como a primeira opçao, o programa nao dá a resposta esperada.Não mostra n1 como maior numero digitado.
        if n1 > n2:
            maior = n1
        else:
            maior = n2
            print('Entre {} e {} o maior número é {}.'.format(n1, n2, maior))
    elif opcao == 4:
        n1 = int(input("Digite um novo valor: "))
        n2 = int(input('Digite um segundo novo valor: '))
    elif opcao == 5:
        print('Terminando programa...')
        sleep(1.5)
    else:
        print('Opção Inválida, tente novamente!!')
    print('=-=' * 10)
print('Fim do programa!!')

