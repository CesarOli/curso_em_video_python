from time import sleep
#Crie um programa que leia vários números e coloque em uma lista
#Depois disso, crie duas listas extras, uma par e uma impar
#Ao Final mostre o conteúdo das três listas geradas.

valores = []
lista_pares = []
lista_impares = []
resposta = ' '

while True:
    valor = int(input('Digite um valor, este valor será incluído em uma única lista: '))
    if valor in valores:
        print('Este valor já consta na lista, informe outro valor: ')
    else:
        valores.append(valor)
        resposta = str(input('Deseja continuar? Informe "S" ou "N": ')).strip().upper()
        if resposta != 'S' and resposta != 'N':
            print('Informe somente "S" ou "N", por favor!')
        elif resposta == 'N':
            break

#incluir valores na lista de números pares e ímpares
for valor in valores :
    if valor % 2 == 0:
        lista_pares.append(valor)
    else:
        lista_impares.append(valor)

sleep(2)
print('\nAguarde, gerando suas listas...')
print(f'A lista consta estes valores {valores} digitados.')
sleep(1)
print('\nGerando lista com números pares. Aguarde!')
sleep(0.5)
print(f'Lista com números pares {lista_pares}')
print('\nGerando lista com números impares.')
sleep(1)
print(f'Lista com números ímpares{lista_impares}')
sleep(1)
print('\nFim do Programa!!')
