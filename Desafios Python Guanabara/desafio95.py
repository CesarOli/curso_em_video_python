#Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo
#um sistema de visualização de detalhes do aproveitamento de cada jogador.
time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Artilheiro: '))
    quantidade_de_partidas = int(input(f'Quantas partidas {jogador["nome"]} artilheiro jogou?: '))
    partidas.clear()

    for c in range(0, quantidade_de_partidas):
        partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
    jogador['partidas'] = partidas[:]
    jogador['total'] = sum(partidas)
    resposta = str(input('Deseja continuar? [S/N]: ')).upper()[0]
    time.append(jogador.copy())

    while True:
        if resposta in 'SN':
            break
        print('ERRO!! Responda somente S ou N.')
    if resposta == 'N':
        break
print('=' * 50)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 50)
for i, k in enumerate(time):
    print(f' {i+1:>4} ', end='')
    for d in k.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)

while True:
    buscar = int(input('Mostrar dados de qual jogador? (999 para sair do programa)'))-1
    if buscar == 999:
        break
    if buscar >= len(time):
        print(f'ERRO!! Jogador com o código {buscar} inexistente.')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[buscar]["nome"]}:')
        for i, g in enumerate(time[buscar]['gols']):
            print(f' No jogo {i+1} fez{g} gols.')
        print('--' * 50)
print('Fim do Programa!!')
