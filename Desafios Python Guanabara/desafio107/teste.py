from moeda import dobro, aumentar, diminuir, metade


valor = float(input('Informe qualquer valor:R$ '))

print(f'Aumentando 10% de {valor}, temos {aumentar(valor, 10)}')
print(f'Reduzindo 13% de {valor}, temos {diminuir(valor, 13)}')
print(f'A metade de {valor}, é {metade(valor)}')
print(f'O dobro de {valor}, é {dobro(valor)}')
