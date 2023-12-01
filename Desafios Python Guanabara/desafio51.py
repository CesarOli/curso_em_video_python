print('\033[1;31mProgração Aritmética.\033[m')
print('Os 10 primeiro TERMOS De Uma PA.\n')
pt = int(input('Informe o Primeiro Termo: '))
razao = int(input('Informe a razão desta PA: '))
decimo = pt + (10 - 1) * razao
for c in range(pt, decimo + razao, razao):
    print(c)
print('ACABOU!!')