#Crie um programa que crie uma matriz da dimensão 3x3
#E preencha com valores lido pelo teclado
#No final, mostre a matriz na tela com a formatação correta.
'''
matriz = [] 
for l in range(3):
    linha = []
    for c in range(3):
        posicao = int(input(f'Informe o valor para a linha da matriz({l}, {c}) '))
        linha.append(posicao)
    matriz.append(linha)

for linha in matriz:
    print(linha)
    '''



# segunda opção de matriz sem a função append()

matriz = [[0, 0, 0],[0, 0, 0, ],[0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para {l}, {c}: '))
for l in range(0, 3):
    for c in range(0, 3):
         print(f'[{matriz [l][c]:^5}]', end='')
    print()

print('Fim do Programa')