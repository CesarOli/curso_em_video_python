print('Aumento no Salário!!\n')
salario = float(input('Diga o salário que eu calculo o valor do seu aumento: R$'))
if salario >= 1250.00:
    salarioNovo = salario + (salario * 10 / 100)
    print('Com aumento de 10%, seu novo salário será de R${:.2f}.'.format(salarioNovo))
else:
    salarioNovo = salario + (salario * 15 /100)
    print('Com o aumento de 15%, seu novo salário será de R${:.2f}.'.format(salarioNovo))
print('\n---fim---')