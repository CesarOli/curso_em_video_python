# Faça um programa que tenha uma lista chamada números e duas funções chamadas
# soteia() e somaPar(). A primeira função vai sortear 5 números e vai coloca-la
# dentro da lista e a segunda função vai mostrar a soma entre todos os valores
# PARES sorteados pela função anterior.

import random
from time import sleep

def sorteia():
    numeros = []
    print(f'Sorteando 5 números de forma aleatória: ', end='')
    for num in range(5):
        numeros_aleatorios = random.randint(1, 100)
        numeros.append(numeros_aleatorios)
        sleep(0.2)
    return (numeros)

def somaPar(numeros):
    soma = 0
    for num in numeros:
        if num % 2 == 0:
            soma += num
    return (soma)

#Programa Principal

numeros = sorteia()
sleep(1)
print(f'Os numeros sorteados foram {numeros}', flush=True)
soma_pares = somaPar(numeros)
sleep(1)
print(f'A soma dos números pares é: {soma_pares}', flush=True)
