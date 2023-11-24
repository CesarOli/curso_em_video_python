from datetime import date
print('\033[1;31mClassificando Atletas.\033[m\n')
nascimento = int(input('Você atleta, digite aqui seu ano de nascimento para identificarmos sua categoria: '))
atual = date.today().year
idade = atual - nascimento
print('Sua idade é {} anos.'.format(idade))
if idade <= 9:
    print('Sua categoria é a MIRIM.')
elif idade <= 14:
    print('Sua categoria é a INFANTIL.')
elif idade <= 19:
    print('Sua categoria é a JUNIOR.')
elif idade <= 25:
    print('Sua categoria é a SÊNIOR.')
else:
    print('Sua categoria é a MASTER.')
print('FIM')
