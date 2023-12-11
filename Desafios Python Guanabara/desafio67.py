print('\033[1;31mTabuada v3.0\033[m')
while True:
    n = int(input('Digite um número para saber sua tabuada, para encerrar digite um número negativo: '))
    if n < 0:
        break
    t = -1
    while t <= 9:
        t += 1
        print(n, ' x', t, ' =', n*t)
print('TABUADA ENCERRADA!')
print('Valeeu!!')

'''while True:
    n = int(input('Digite um número para saber sua tabuada, para encerrar, digite um número negativo: '))
    if n < 0:
        break
    for c in range(1, 11):
        print(n, ' x', c, ' =', n*c)
print('TABUADA ENCERRADA!!')
print('Valeu!!')'''

