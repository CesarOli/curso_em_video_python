print('\033[1;31mProgressão Aritmética v2.0\033[m')
pt = int(input('Informe o primeiro termo da Progressão Aritmética que deseja saber: '))
razao = int(input('Informe a razao desta PA: '))
contador = 1
termo = pt
while contador <= 10:
    print('{} -> '.format(termo), end='')
    termo = termo + razao
    contador = contador + 1
print('Finalizado!!')
