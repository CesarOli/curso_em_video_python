from time import sleep
#Crie um programa onde o usuário possa digitar cinco valores numéricos e
#cadastre-os em uma lista já na posição correta de inserção (Sem usar o sort())
#No final, mostre a lista ordenada na tela.


valores = []
for v in range(0, 5):
    valor = int(input('Digite um valor: '))
    if v == 0 or valor > valores[-1]:
        valores.append(valor)
        print('Número adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(valores):
            if valor <= valores[pos]:
                valores.insert(pos, valor)
                print(f'Número adicionado na posição {pos} da lista.')
                break
            pos += 1
print('Aguarde estamos gerando sua lista.')
sleep(2)
print(valores)
sleep(1)
print('Fim do Programa!!')
        