#Crie um programa que gerencie o aproveitamento de um jogador de futebol.
#O programa vai ler o nome do jogador, e quantas partidas e jogou.
#Depois, vai ler a quantidade de gols feito em cada partida.
#No final, tudo isso será guardado em um dicionário, incluindo o
#Total de gols feito durante o campeonato.

jogador = dict()
gols = []

jogador['Nome'] = str(input('Diga o nome do artilheiro: '))
quantidade_de_partidas = int(input('Quantas partidas este artilheiro jogou: '))

for g in range(0, quantidade_de_partidas):
    gols.append(int(input(f'Quantos gols na partida {g+1}: ')))

jogador['Gols'] = gols
jogador['total'] = sum(gols)

print('=' * 50)
print(jogador)
print('=' * 50)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')

print('=' * 50)
print(f'O jogador {jogador["Nome"]}, jogou {len(jogador["Gols"])} jogos.')

for i, v in enumerate(jogador['Gols']):
    print(f'Na partida {i+1} fez {v}')
print(f'Foi um total de {jogador["total"]} gols.')
