from random import randint
from time import sleep
print('\033[1;31mVAMOS JOGAR JOKEMPÔ!!\033[m')
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Jogada: 
[ 0 ] PEDRA
[ 1 ] PAPEL 
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua? '))
print('\033[1;34mJO\033[m')
sleep(1)
print('\033[1;36mKEN\033[m')
sleep(1)
print('\033[1;33mPÔ!!\033[m')
sleep(1.5)
print('-=' * 15)
print('O Computador jogou {}'.format(itens[computador]))
print('O Jogador jogou {}'.format(itens[jogador]))
print('-=' * 15)
if computador == 0: # computador jogou PEDRA
    if jogador == 0:
        print('\033[33mEMPATE\033[m')
    elif jogador == 1:
        print('\033[32mJOGADOR VENCEU.\033[m')
    elif jogador == 2:
        print('\033[31mCOMPUTADOR VENCEU.\033[m')
    else:
        print('\033[7;40mJOGADA INVÁLIDA!!\033[m')
elif computador == 1: # computador jogou PAPEL
    if jogador == 0:
        print('\033[31mCOMPUTADOR VENCEU.\033[m')
    elif jogador == 1:
        print('\033[33mEMPATE\033[m')
    elif jogador == 2:
        print('\033[32mJOGADOR VENCEU.\033[m')
    else:
        print('\033[7;40mJOGADA INVÁLIDA!!\033[m')
elif computador == 2: # computador jogou TESOURA
    if jogador == 0:
        print('\033[32mJOGADOR VENCEU.\033[m')
    elif jogador == 1:
        print('\033[31mCOMPUTADOR VENCEU.\033[m')
    elif jogador == 2:
        print('\033[33mEMPATE\033[m')
    else:
        print('\033[7;40mJOGADA INVÁLIDA!!\033[m')
print('\n\033[32mFim de Jogo.\033[m')
