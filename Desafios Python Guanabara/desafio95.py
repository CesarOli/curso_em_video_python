#Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo
#um sistema de visualização de detalhes do aproveitamento de cada jogador.
time = []
jogador = dict()
gols = []
partidas = ()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Artilheiro: '))
    quantidade_de_partidas = int(input(f'Quantas partidas {jogador["nome"]}o artilheiro jogou?: '))

    for g in range(0, quantidade_de_partidas):
        gols.append(int(input(f'Quantos gols na partida {g+1}: ')))
    jogador['Gols'] = partidas[:]
    jogador['total'] = sum(gols)
    resposta = str(input('Deseja continuar? [S/N]: ')).upper()[0]
    time.append(jogador.copy())

    while True:
        if resposta in 'SN':
            break
        print('ERRO!! Responda somente S ou N.')
    if resposta == 'N':
        break
print('=' * 50)
for i, k in enumerate(time):
    print(f' {k:>3}', end='')
    for d in i.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
