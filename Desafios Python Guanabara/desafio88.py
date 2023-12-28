from random import randint
from time import sleep

# Faça um programa que ajude um jogador da MEGA SENA criar palpites
# O programa vai perguntar quantos jogos serão gerados 
# E sortear sortear 6 números entre 1 e 60 para cada jogo
# cadastrando tudo em uma lista composta.

loteria = []
jogos = []

quantidade_de_jogos = int(input('Quantos jogos você deseja fazer: '))
total_de_jogos_sorteados = 1 

while total_de_jogos_sorteados <= quantidade_de_jogos:
    contador = 0
    while True:
        num = randint(1, 60)
        if num not in loteria:
            loteria.append(num)
            contador += 1
        if contador >= 6:
            break
    loteria.sort()

    jogos.append(loteria[:])
    loteria.clear()
    total_de_jogos_sorteados += 1

for valor, linha in enumerate(jogos):
    print(f'Jogo {valor + 1}: {linha}')
    sleep(1)
