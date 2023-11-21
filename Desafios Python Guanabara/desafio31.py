'''distancia = float(input('Qual a distância da sua próxima viagem, favor informar em KM: '))
if distancia >= 200:
    preco = distancia * 0.45
    print('Sua passagem pra distância de {:.0f}Km, vai ficar em R${:.2f}.'.format(distancia, preco))
else:
    preco = distancia * 0.50
    print('Sua passagem pra distância de {:.0f}KM, vai ficar em R${:.2f}.'.format(distancia, preco))
print('---MODELO SIMPLIFICADO---\n')'''

distancia = float(input('Qual é a distância da sua próxima viagem? '))
preco = distancia * 0.45 if distancia >=200 else distancia * 0.50
print('O preço da sua passagem será de R${:.2f}.'.format(preco))