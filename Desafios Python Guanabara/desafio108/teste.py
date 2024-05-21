import moeda

valor = float(input('Informe qualquer valor: '))

print(f'Aumentando 10% de {moeda.moeda(valor)}, temos {moeda.moeda(moeda.aumentar(valor, 10))}')
print(f'Reduzindo 13% de {moeda.moeda(valor)}, temos {moeda.moeda(moeda.diminuir(valor, 13))}')
print(f'A metade de {moeda.moeda(valor)}, é {moeda.moeda(moeda.metade(valor))}')
print(f'O dobro de {moeda.moeda(valor)}, é {moeda.moeda(moeda.dobro(valor))}')

