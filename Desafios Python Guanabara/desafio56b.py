print('\033[1;37mAnalisador de Cadastro versão 1.0\033[m')
mediaIdade = 0
maisVelho = 0
nomeVelho = ''
totalMulher20 = 0
for cadastro in range(1, 5):
    print('\n=== {}° Pessoa ==='.format(cadastro))
    nome = input('Digite o nome: ').strip()
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite seu sexo: [M/F]: ').strip().upper()
    mediaIdade += idade
    if cadastro == 1 and sexo in 'M':
        maisVelho = idade
        nomeVelho = nome
    if sexo in 'M' and idade > maisVelho:
        maisVelho = idade
        nomeVelho = nome
    if sexo in 'F' and idade < 20:
        totalMulher20 += 1
print('A média de idade deste grupo de pessoas é {}.'.format(mediaIdade / 4))
print('O homem mais velho é o {} com, {} anos.'.format(nomeVelho, maisVelho))
print('A quantidade de mulheres com menos de 20 anos é {}.'.format(totalMulher20))
print('---FIM---')

