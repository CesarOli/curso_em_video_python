print('\033[1;31mJogo de Adivinhação v2.0\033[m')
from random import randint
from time import sleep
print('Olá humano, sou seu computador, eu pensei em um número e quero saber se você consegue descobrir qual foi')
num = 0
computador = randint(1, 11)
contador = 0
while num != computador and contador < 11:
    num = int(input('Tenta aí: '))
    contador += 1
    if num == computador:
        print('Aconteceu um milagre, o humano venceu...ahahahaha')
    else:
       if num < computador:
           print('Mais...tente mais uma vez')
       elif num > computador:
           print('Menos, tente mais uma vez')
print('Humano, você usou {} tentativas para vencer o computador.'.format(contador))
print('FIM')
