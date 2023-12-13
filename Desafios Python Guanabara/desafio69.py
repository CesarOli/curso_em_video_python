print('\033[1;31mAnalisando Dados Em Grupo\033[m\n')
print('Cadastro Simples de Pessoa Física\n')
totalH = mulherMenos20 = total18 = 0
while True:
    idade = int(input('Informe sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Somente M/F: ')).strip().upper()[0]
    if idade >= 18:
        total18 += 1
    if sexo == 'M':
        totalH += 1
    if sexo == 'F' and idade < 20:
        mulherMenos20 += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar S ou N: ')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'A quantidade de pessoas com mais de 18 anos é de {total18}.')
print(f'A quantidade de homens cadastrados foi de {totalH}.')
print(f'A quantidade de mulheres menores de 20 anos é {mulherMenos20}')
print('FIM')
