from time import sleep
print('\033[1;31mTratando vários Valores\033[m')
sleep(0.9)
print('Olá, seja muito bem vindo ao meu Programa de Estudos do César.')
sleep(2)
print('Para encerrar o programa, digite 999.')
sleep(1)
n = soma = count = 0
while n != 999:
    n = int(input('Informe um número inteiro, por favor: '))
    if n != 999:
        soma = soma + n
        count = count + 1
print('A quantidade de números digitados foi de {}, e a soma entre eles é de {}.'.format(count, soma))
print('\033[1:34mObrigado, fim do programa!\033')
