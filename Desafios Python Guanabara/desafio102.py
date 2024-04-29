# Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o numero a calcular e o outro chamado show, que será
# um valor lógico(opcional)indicando se será mostrado ou não na tela o processo
# de cálculo do fatorial.

def fatorial(num=1, show=False):
    """
    -> Calcula o fatoria de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou nao a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show: 
            if c != 1:
                print(f'{c} x ', end='')
            else:
                print(f'{c} = ', end='')
    return f


num = int(input('Digite um número para saber o seu fatorial: '))
mostrar_processo = input('Deseja mostrar o processo de cálculo? [S/N]').strip() .upper()

resultado = fatorial(num)
if mostrar_processo == 'S':
    resultado = fatorial(num, show=True)
else:
    resultado = fatorial(num)
print(f'O fatorial do numero informado é {resultado}.')
help(fatorial)