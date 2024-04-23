# Faça um programa que tenha uma função chamada area(), e que receba 
# as dimensões retangular(Largura e cumprimento) e mostre área do terreno.

def l():
    print('-' * 30)

def p_l():
    print('\n')

largura = float(input('Informe a largura do terreno: '))
cumprimento = float(input('Informe o comprimento do terreno: '))


def area(largura, cumprimento):
    tamanho = largura * cumprimento
    print(f'Um terreno com a largura de {largura} metros, com o cumprimento de {cumprimento} metros, tem a área total de {tamanho} metros quadrados.')

p_l()
l()
print('Controle da área do terreno.')
l()
p_l()

area(largura, cumprimento)
p_l()