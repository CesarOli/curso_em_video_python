from time import sleep

#Crie um programa onde o usuário possa digitar
# vários valores númericos e cadastre-os em uma lista
#Caso o número já exista na lista, ele não poderá ser
#adicionado novamente.
#Ao final, serão exibidos todos os valores únicos 
#digitados em ordem crescente.

valores = []
resposta = ''

while True:
    valor = int(input('Digite um valor: '))
    if valor in valores:
        print('Este valor já consta na lista, Informe outro número, por favor!')
    else:
        valores.append(valor)

    resposta = str(input('Deseja continuar, s ou n: ')).strip().upper()
    if resposta != 'N' and resposta != 'S':
        print('Digite somente "s" para SIM, ou "n" para NÃO, por favor: ')
    elif resposta == 'N':
        break
print('Gerando sua lista de valores...Aguarde!!')
sleep(2)
print(sorted(valores))
print('Aguarde, finalizando o programa.')
sleep(1.8)
print('Fim do Programa, obrigado!')
