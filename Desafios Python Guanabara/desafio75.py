from time import sleep

# Desenvolva um programa que leia quatro valores 
# pelo teclado e guarde-os em um tupla.
# No final, mostre:
#A) quantas vezes apareceu o valor 9
#B) em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

#OBS: PROCURAR POR MÉTODOS NO PYTHON QUE TRAGA A SOLUÇÃO, como por exemplo
# o método count() e/ou o método index()

print('Você vai precisar informar quatro números.')
numeros = []
for _ in range(4):
    numero = int(input('Informe um número: '))
    numeros.append(numero)
tupla_de_numeros = tuple(numeros)

print(f'Voce digitou ous números {tupla_de_numeros}')
print(f'O número 9 apareceu {tupla_de_numeros.count(9)}.')

'''c = 0
for numero in tuplas_de_numeros:
    if numero == 9:
        c += 1
print(f'O número 9 apareceu {c} vezes na tupla.')
'''

encontra_o_tres = None
for c, numero in enumerate(tupla_de_numeros):
    if numero == 3:
        encontra_o_tres = c 
        break
sleep(1)
if encontra_o_tres is not None:
    print(f'O primeiro número três encontrado está na posição {c+1}.')
else: 
    print(f'O número três não foi encontrado na tupla.')
print('Os valores pares digitados foram ', end='')
for numero in tupla_de_numeros:
    if numero % 2 == 0:
        print(numero, end=' ')
