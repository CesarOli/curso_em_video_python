import random
titulo = '\nChamando a biblioteca inteira.\n'
print(titulo.upper())
aluno1 = input('Nome do primeiro aluno: ')
aluno2 = input('Nome do segundo aluno: ')
aluno3 = input('Nome do terceiro aluno: ')
aluno4 = input('Nome do quarto aluno: ')

lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(lista)
print('O aluno escolhido foi: {}!\nObrigado!'.format(escolhido))

from random import choice
titulo = '\nChamando somente o método direto da biblioteca.\n'
print(titulo.upper())
aluno1 = input('nome do primeiro aluno: ')
aluno2 = input('nome do segundo aluno: ')
aluno3 = input('nome do terceiro aluno: ')
aluno4 = input('nome do quarto aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = choice(lista)
print('O aluno escolhido foi: {}!\nObrigado'.format(escolhido))