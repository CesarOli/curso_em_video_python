print('\033[1;31mSequencia de Fibonacci.\033[m')
n = int(input('Quantos termos da Sequência de Fibonacci você deseja visualizar? '))
f1 = 0
f2 = 1
print('{} -> {}'.format(f1, f2), end='')
cont = 3
while cont <= n:
    f3 = f1 + f2
    print(' -> {}'.format(f3), end='')
    f1 = f2
    f2 = f3
    cont += 1
print(' -> FIM')


