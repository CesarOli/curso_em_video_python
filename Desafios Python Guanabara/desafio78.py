from time import sleep

#Faça um programa que leia 5 valores numéricos
#e guarde em uma lista
#No final mostre qual foi o maior 
#e o menor valor digitado
#e as suas respectivas posições

valores = []
for c in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print(valores)

maior_valor = max(valores)
menor_valor = min(valores)

for cont, v in enumerate(valores):
    if v == maior_valor:
        print('Aguarde, estamos processando o MAIOR e o MENOR valor digitado.')
        sleep(2)
        print(f'O maior valor encontrado nesta lista foi o {maior_valor}, e ele esta na posição {cont}.')
    elif v == menor_valor:
        print(f'...e o menor valor encontrado nesta lista foi o {menor_valor}, e ele esta na posição {cont}')
print('Fim do Programa!!')