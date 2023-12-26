# Aprimore o desafio anterior, mostrando no final:
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.


matriz = [[0, 0, 0],[0, 0, 0, ],[0, 0, 0]]
soma_todos_os_pares = soma_terceira_coluna = maior_valor_segunda_linha = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para {l}, {c}: '))
        if matriz[l][c] % 2 == 0:
            soma_todos_os_pares += matriz[l][c]
        if c == 2:
            soma_terceira_coluna += matriz[l][c]
        if l == 1:
            if maior_valor_segunda_linha is None or matriz[l][c] > maior_valor_segunda_linha:
                maior_valor_segunda_linha = matriz[l][c]

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz [l][c]:^5}]', end='')
    print()
print(f'A soma dos números pares digitados é: {soma_todos_os_pares}')
print(f'A soma dos valores da terceira coluna é {soma_terceira_coluna}')
print(f'o maior valor digitado na segunda linha foi: {maior_valor_segunda_linha}')
print('Fim do Programa')
