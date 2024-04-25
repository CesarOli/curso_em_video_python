# Faça um programa que tenha uma função chamada maior(), que receba vários 
# parâmetros com valores inteiros.
# Este programa tem que analisar todos os valores e dier qual deles é o maior. 
from time import sleep


def maior(*numeros):
    maior = c = 0
    print('Analisando os números informados, temos: ')
    for valor in numeros:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if c == 0:
             maior = valor
        else:
            if valor > maior:
                maior = valor
        c += 1
    print(f'Foram informados {c} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')
    

#Programa Principal  
maior(10, 5, 8, 20, 15)
maior(34, 2, 303, 4040595, 3048034982435)