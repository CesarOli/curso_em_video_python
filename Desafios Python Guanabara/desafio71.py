print('\033[1;31mSimulando um Caixa Eletrônico\033[m')
saque = int(input('Valor do Saque: R$'))
# notas de 100, 50, 20, 10, 2, 1 real
valorSaque = saque
cedula = 50
totalCed = 0
while True:
    if valorSaque >= cedula:
        valorSaque -= cedula
        totalCed += 1
    else:
        if totalCed > 0:
            print(f'O total de {totalCed} de cédulas de {cedula}')
        if 

    elif valorSaque == 50:
            cedula = 20
            totalCed += 1
    else:
        break
print(f'Você receberá {totalCed} de 50 reais.')
print(f'Você receberá {totalCed} de 20 reais.')
print('FIM')

