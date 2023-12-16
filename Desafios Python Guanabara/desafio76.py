from time import sleep

#Crie um programa que tenha uma tupla 
#única com nomes de produtos e seus 
#respectivos preços na sequencia
#no final, mostre uma listagem de
#preços organizando os dados em 
#forma tabular.


precos_e_produtos = ('xícara', 5.90, 
                     'Garrafa D"água"', 65.40, 
                     'caneta bic', 1.50,
                     'caderno 150 folhas', 12.90, 
                     'pinça', 5.60, 
                     'toalha de mesa', 56.90, 
                     'carrinho de brinquedo', 22.90,
                     'fruteira', 15.9,
                     'teclado de computador',122.99,
                     )
sleep(0.3)
print('LISTA DE PRODUTOS E SEU VALORES\n')
sleep(2.5)
print('Por favor, aguarde, estamos organizando a lista de preços.\n')
sleep(2.5)
print('------------------------------------------------------------')
print('Produto                                                Preço')
sleep(0.5)
print('------------------------------------------------------------\n')
for i in range(0, len(precos_e_produtos)):
    if i % 2 == 0:
        sleep(0.5)
        print(f'{precos_e_produtos[i]:.<30}', end='')
    else:
        print(f'R${precos_e_produtos[i]:>7.2f}')    
sleep(1)
print('\nLista completa.')
sleep(1.5)
print('Fim do programa!')