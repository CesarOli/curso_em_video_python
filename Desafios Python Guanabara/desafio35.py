from time import sleep
print('\033[1;31mAnalisando Triângulos v1.0.\033[m')
print('\nInforme o valor de três retas afim de saber se É ou NÃO possível formar um triângulo: ')

r1 = float(input('\nvalor da primeira reta: '))
r2 = float(input('valor da segunda reta: '))
r3 = float(input('valor da terceira reta: '))
print('PROCESSANDO...')
sleep(1.5)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 +r2:
    print('Sim, é possível formar um Triângulo, Parabéns!!!')
else:
    print('Não, não é possível construir um Triângulo.')
print('---fim---')

