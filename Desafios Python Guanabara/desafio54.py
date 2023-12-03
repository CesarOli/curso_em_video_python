from datetime import date
print('\033[1;31mGrupo da Maioridade.\033[m')
ano = date.today().year
maior = 0
menor = 0
nascimento = 0
for grupo in range(1, 8):
    nascimento = int(input('Digite a data de nascimento da {}º pessoa: '.format(grupo)))
    if ano - nascimento >= 21:
        maior = maior + 1
    else:
        menor = menor + 1
print('A quantidade de pessoas menores de idade é {}.'.format(menor))
print('...e a quantidade de pessoas  que atingiram a maior é de \033[32m{}\033[m pessoas.'.format(maior))
print('FIM')
