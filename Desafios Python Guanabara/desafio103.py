# Faça um programa que tenha uma função chamada ficha(), que receba dois 
# parâmetros opcionais: O nome de um jogador e quantos gols ele marcou. 
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que 
# algum dado não tenha sido informado corretamente.

def ficha(nome="<desconhecido>", gols=0):
    print(f'O jogador {nome} marcou {gols} gol(s) no campeonato atual.')
   


nome = input('Digite o nome do Jogador: ')
gols = input('Quantos gols este jogador marcou ao total: ')

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip()== '':
    ficha(gols=gols)
else:
    ficha(nome, gols)
