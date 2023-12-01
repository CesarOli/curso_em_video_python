print('\033[1;31mTabuada, v.2.0\033[m')
numero = int(input('Informe um número para saber sua Tabuada: '))
for c in range(0, 11):
    tabuada = numero * c
    print('{} x {:2} = {}'.format(numero, c, tabuada))