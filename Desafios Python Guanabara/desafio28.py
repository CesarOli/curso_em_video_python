from random import randint
from time import sleep
num = randint(0, 5)
usuario = int(input('Adivinhe o número que o computador "pensou": '))
print('Processando...')
sleep(2.5)
if usuario == num:
    print('Parabéns, você venceu o computador!!')
else:
    print('O Computador Venceu!!')
print('---FIM---')