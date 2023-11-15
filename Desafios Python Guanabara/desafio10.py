reais = float(input('Quanto você tem na carteira pra comprar de dolares? R$ '))
dolar = reais / 5.18
euro = reais / 5.31
libra = reais / 6.35


print('Com R${} reais \nVocê consegue comprar U${:.2f} dolares. '.format(reais, dolar))
print('Com R${} reais \nVocê consegue comprar E${:.2f} euros '.format(reais, euro))
print('Com R${} reais \nVocê consegue comprar L${:.2f} libras '.format(reais, libra))
