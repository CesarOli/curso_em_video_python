from operator import itemgetter
from time import sleep
from random import randint
#Crie um programa onde 4 jogadores joguem um dado e tenha resultados aleatórios.
#Guarde esses resultados em um dicionário. Ao Final, coloque esse dicionário 
#em ordem sabendo que o vencedor tirou o maior número no dado.
'''
quantidade_jogadores =  4
resultados = {}

for jogador in range(1, quantidade_jogadores + 1):
    resultado = randint(1, 6)
    resultados[f'Jogador {jogador}'] = resultado

sleep(0.5)
print('Resultado dos Lançamentos:')

for jogador, resultado in resultados.items():
    sleep(0.7)
    print(f'{jogador}: {resultado}')

resultados_ordenados = sorted(resultados.items(), key=lambda x: x[1], reverse=True)

resultado_final_ordenado = {}
for jogador, resultado in resultados_ordenados:
    resultado_final_ordenado[jogador] = resultado

print('\nDicionário Ordenado:')
for jogador, resultado in resultado_final_ordenado.items():
    print(f'{jogador}: {resultado}')

jogador_vencedor, resultado_vencedor = resultado_final_ordenado.values()
print(f'\nO vencedor é {jogador_vencedor} com {resultado_vencedor}')


print('Fim do Programa')
'''

jogo = {'Jogador1': randint(1, 6),
        'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6),
        'Jogador4': randint(1, 6)
}

ranking = []

print('Valores Sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)


for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
print('Fim do Programa')
