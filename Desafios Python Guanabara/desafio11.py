a = float(input('informe a altura da sua parede: '))
b = float(input('Informe a largura da sua parede: '))
area = a * b
quantidadeTinta = area / 2
print('Sua área totoal é de {:.2f}, e a quantidade necessária de tinta para pintar é de {:.0f} litros. '.format(area, quantidadeTinta))