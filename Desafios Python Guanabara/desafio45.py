import random
print('\033[1;31mJogando Jokempô\033[m\n')
print('Vamos jogar JOKEEEMPÔ, pô!!')

escolha = int(input('''Escolha: 
[ 1 ] TESOURA
[ 2 ] PAPEL 
[ 3 ] PEDRA 
sua escolha: '''))
computador = random.randint(1, 3)
if computador == 1 and escolha == 2:
    print('O computador venceu, tente novamente!!')
elif computador == 1 and escolha == 3:
    print('Você Venceeeuu!!')
elif computador == 2 and escolha == 1:
    print('Você Venceeeuu!!')
elif computador == 2 and escolha == 3:
    print('O computador venceu, tente novamente!!')
elif computador == 3 and escolha == 1:
    print('O computador venceu, tente novamente!!')
elif computador == 3 and escolha == 2:
    print('Você Venceeeuu!!')
