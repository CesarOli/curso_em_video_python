from time import sleep

#Crie um programa que leia vários numeros e coloque em uma lista.
#Depois disso, mostre:
#A) Quantos números foram digitados
#B) A lista de valores ordenada de forma descrescente
#C) Se o valor 5 foi digitado, e está ou não na lista.

valores = []
resposta = ' '

while True:
    valor = int(input('Digite um valor: '))

    if valor in valores:
        print('Esse valor já existe na lista. Informe outro valor!!')
    else:
        valores.append(valor)
    resposta = str(input('Deseja continuar incluindo números na lista, "S" ou "N"?: ')).strip().upper()
    if resposta != 'S' and resposta != "N":
        print('Digite somente "S" ou "N", por favor:')
    elif resposta == 'N':
        break

print('Gerando sua lista com elementos digitados....Aguarde!')
sleep(1)
print(valores)
print(f'Foram digitados {len(valores)} valores nesta lista.')
valores.sort(reverse=True)
print('Aguarde, gerando lista em ordem decrescente...')
print(f'Lista em ordem decrescente: ', valores)
sleep(2)
if 5 in valores:
    print('O elemento 5 faz parte da lista.')
else:
    print('Não foi encontrado o valor 5 nesta lista.')
print('Fim do Programa')
