import random
from time import sleep

# Crie um programa que gere cinco números aleatórios
# e coloque em uma tupla
# Depois disso, mostre a listagem de números gerados
#e também indique o menor e o maior valor que estão 
#na tupla

#É POSSIVEL USAR O método MAX E MIN da tupla para saber o maior e menor elemento randomizado em cada tupla

sorteio = tuple(random.randint(0, 9) for _ in range(5))

print(sorteio)

'''maior = sorteio[0]
menor = sorteio[0]
for numero in sorteio:
    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero
print('Processando....')
sleep(0.5)
print(f'O maior número encontrado foi {maior} ')
sleep(0.5)
print(f'O menor número encontrado foi {menor}')'''

print(f'O maior elemento da tupla é {max(sorteio)}')
print(f'...e o menor elemento da tupla é {min(sorteio)}')


