#Faça um programa que leia nome e peso de várias pessoas
#Guardando tudo em uma lista
#Ao final mostre:
#Quantas pessoas foram cadastradas;
#Uma listagem com as pessoas mais pesadas
#Uma listagem com as pessoas mais leves

lista_temporaria = []
lista_principal = []
mai = men = 0

while True:
    lista_temporaria.append(str(input('Nome: ')))
    lista_temporaria.append(float(input('Peso:')))
    if len(lista_principal) == 0:
        mai = men = lista_temporaria[1]
    else:
        if lista_temporaria[1] > mai:
            mai = lista_temporaria[1]
        if lista_temporaria[1] < men:
            men = lista_temporaria[1]
    lista_principal.append(lista_temporaria[:])
    lista_temporaria.clear()
    resposta = str(input('Deseja continuar: "S" ou "N": '))
    if resposta in 'Nn':
        break
print(f'Ao todo foram cadastrados {len(lista_principal)} pessoas.')
print(f'O maior peso foi de {mai}kg. Peso de ', end='')
for pessoa in lista_principal:
    if pessoa[1] == mai:
        print(f'[{pessoa[0]}]', end='')
print()
print(f'O menor peso foi de {men}kg. Peso de ', end='')
for pessoa in lista_principal:
    if pessoa[1] == men:
        print(f'[{pessoa[0]}]', end='')
print()

