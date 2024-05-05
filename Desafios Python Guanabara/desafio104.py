# Faça um programa que tenha a função leiaint(), que vai funcionar de forma 
# semelhante a função input() do Python, só que fazendo a validação para
# aceitar apenas um valor numérico
# Ex.: n = leiaint('Digite um número:')
'''from time import sleep

# Minha solução:

def leiaint(numero):
    while True:
        try:
            entrada = int(input(numero))
            sleep(0.8)
        except ValueError:
            print('Erro: por favor, digite um valor inteiro válido!')
        else:
            return entrada

n = leiaint('Digite um número: ')
print(f'Obrigado, voce digitou o número {n}.')'''


# Solução do Professor (Gustavo Guanabara)
def leiaint(numero):
    ok = False
    valor = 0
    while True:
        n = str(input(numero))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0:32mErro! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor

# Programa Principal
n = leiaint("Digite um número: ")
print(f'Você digitou o numero {n}')

