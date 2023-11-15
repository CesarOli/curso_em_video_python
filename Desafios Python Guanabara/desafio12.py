preço = float(input('Por favor, informe o valor do produto: R$ '))
desconto= preço * 5 / 100
novoPreço = preço - desconto
print('O produto que custava {:.2f}, na promoção com 5% de desconto vai custar R$ {:.2f} '.format(preço, novoPreço))