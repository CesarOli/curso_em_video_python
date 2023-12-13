import random
print('VAMOS JOGAR PAR OU ÍMPAR?!?!')
v = 0
while True:
    n = int(input('Digite um número de 0 a 10 para ganhar do computador no Par ou Ímpar: '))
    computador = random.randint(0, 10)
    total = n + computador
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Você escolhe P ou I: ')).upper().strip()[0]
    print(f'Você escolheu {n}, o computador escolheu {computador}, e o total foi de {total}.')
    print('Deu PAR.' if total % 2 == 0 else 'Deu ÍMPAR.')
    if escolha == 'P':
        if total % 2 == 0:
            v += 1
            print('Parabéns, você veeenceu!!!')
        else:
            break
    if escolha == 'I':
        if total % 2 == 1:
            v += 1
            print('Parabéns, você veeenceeuuu!!!')
        else:
            break
print(f'Você venceu o computador {v} vezes, mas essa...')
print('...você perdeu, tente novamente...')
print('GAME OVER, marrecô!!!')
print('FIM')
