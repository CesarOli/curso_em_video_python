# Crie um programa onde o usuário possa digitar sete valores numéricos
# E cadastre-os em uma lista única  
# Separados os valores Pares e Impares. 
# No final, mostre os valores pares e impares em ordem crescente.

valores= [[], []]
numeros = 0
for c in range(1, 8):
    numeros = int(input(f'Digite o {c}º número: '))
    if numeros % 2 == 0:
        valores[0].append(numeros)
    else:
        valores[1].append(numeros)
        
valores[0].sort()
valores[1].sort()
print(f'Os valores pares digitados foram {valores[0]}')
print(f'Os valores ímpares digitados foram {valores[1]}')
