dias = float(input('Informe a quantidade de dias para aluguel do carro: '))
km = float(input('Informe aproximadamente quantos KM pretende rodar com o carro: '))
totalApagar = (dias * 60) + (km * 0.15)
print('O valor total a ser pago será de {:.2f}'.format(totalApagar))
