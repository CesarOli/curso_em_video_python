from datetime import date
print('\033[1;31mAlistamento Militar\033[m\n')

atual = date.today().year
sexo = str(input('Digite aqui seu sexo, "M" para Masculino ou "F" para Feminino: ')).strip().upper()
nascimento = ' '
if sexo == 'F':
    print('O alistamento é obrigatório somente para o sexo Masculino.\nObrigado!')
else:
    sexo == 'M'
    nascimento = int(input('Informe o ano do seu nascimento, por favor: \n'))
    idade = atual - nascimento
    if idade > 18:
        saldo = idade - 18
        print('Voce deveria ter se alistado há {} anos.'.format(saldo))
    elif idade < 18:
        saldo = 18 - idade
        print('Você está com {} anos, faltam {} anos para o seu alistamento, sua hora vai chegar, '
              '\nFIQUE TRANQUILO!!'.format(idade, saldo))
    else:
        print('Voce deve se alistar IMEDIATAMENTE.')
print('\n\033[1;31mFIM.\033[m')