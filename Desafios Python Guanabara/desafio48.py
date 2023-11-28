print('\033[1;31mSomando números múltiplos de 3.\033[m\n ')
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print('A soma dos {} números entre 0 e 500 é de {}.'.format(cont, soma))
