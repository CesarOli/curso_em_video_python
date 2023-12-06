print('\033[1;31mValidação de Dados.\033[m')
sexo = ''
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Informe qual o seu sexo [F/M]: ')).strip().upper()
    print('Favor informar somente "M" ou "F". Tente novamente!!')
print('Sexo {}, cadastrado com sucesso.'.format(sexo))
print('FIM')
'''sexo = str(input('Informe seu sexo [F/M]: ')).strip().upper()
while sexo not in 'FM':
    sexo = str(input('Dados inválidos, tente novamente!! [M/F]: ')).strip().upper()
print('Sexo registrado com sucesso.')
print('FIM')
'''
