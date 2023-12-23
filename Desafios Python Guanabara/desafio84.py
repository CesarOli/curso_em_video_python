from time import sleep

#Faça um programa que leia nome e peso de várias pessoas
#Guardando tudo em uma lista
#Ao final mostre:
#Quantas pessoas foram cadastradas;
#Uma listagem com as pessoas mais pesadas
#Uma listagem com as pessoas mais leves
pessoas_temp = list()
pessoas_final = list()
leves = pesadas = 0
resposta = ''


while True:

     pessoas_temp.append(str(input('Digite seu nome: ')))
     pessoas_temp.append(float(input('Digite seu peso: ')))
     if len(pessoas_final) == 0:
          pesadas = leves = pessoas_temp[1]
     else:
          if pessoas_temp[1] > pesadas:
               pesadas = pessoas_temp[1]
          if pessoas_temp[1] < leves:
               leves = pessoas_temp[1]
     
     pessoas_final.append(pessoas_temp[:])
     pessoas_temp.clear()

     resposta = str(input('Deseja continuar? Informe "S" ou "N": ')).strip().upper()

     while resposta != 'S' and resposta != 'N':
          print('Informe somente "S" ou "N", por favor!')
          resposta = str(input('Deseja continuar? S/N: ')).strip().upper()
     if resposta == 'N':
          break
print('=' * 50)
print(f'No total, foram cadastradas {len(pessoas_final)} pessoas.')
print(f'O maior peso foi de {pesadas}kg.Peso de ', end='')
for p in pessoas_final:
     if p[1] == pesadas:
          print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {leves}kg. Peso de ', end='')
for p in pessoas_final:
     if p[1] == leves:
          print(f'[{p[0]}]', end='')

print()

print('Aguarde, finalizando o programa!!')
sleep(1)
print('Fim do Programa!!')