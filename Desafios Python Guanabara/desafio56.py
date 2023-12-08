print('\033[1;31mAnalisador Completo.\033[m')
mediaIdade = 0
cadastro = 1
maiorHomem = 0
nomeVelho = ''
totalMulher20 = 0
for cadastro in range(1, 5):
    nome = str(input('Escreva aqui o nome completo da {}º pessoa do cadastro: '.format(cadastro))).strip()
    primeiro = nome.split()
    idade = int(input('Diga também a idade desta pessoa, por favor: '))
    sexo = input('Informe seu sexo, "M" para Masculino, "F" para Feminino: ').upper()
    if sexo != 'M' and sexo != 'F':
        print('\n\033[4;31mSexo somente "M" ou "F". Tente Novamente, obrigado!!.\033[m')
    else:
        mediaIdade += idade
    if cadastro == 1 and sexo in 'M':
        maiorHomem = idade
        nomeVelho = nome
    if sexo in 'M' and idade > maiorHomem:
        maiorHomem = idade
        nomeVelho = nome
    if sexo in 'F' and idade < 20:
        totalMulher20 += 1
print('A média da idade das pessoas cadastradas é de {:.0f} anos.'.format(mediaIdade / cadastro))
print('O homem mais velho tem {} anos, e se chama {}.'.format(maiorHomem, nomeVelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totalMulher20))
print('FIM')
