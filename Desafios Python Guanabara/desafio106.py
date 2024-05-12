# Faça um mini-sistema que utilize o interactive Help do Python. O usuário vai 
# digitar o comando e o manual vai aparecer. Quando o usuário digitar palavra
# FIM', o programa se encerrará.

#Obs: Usar cores
from time import sleep

cores = ('\033[m',        # 0 - sem cor
         '\033[30;41m',   # 1 - vermelho
         '\033[30;42m',   # 2 - verde
         '\033[30;43m',    # 3 - amarelo
         '\033[30;44m',    # 4 - azul
         '\033[30;45m',    # 5 - roxo
         '\033[7;30m'     # 6 - branco
         )

def ajuda(comando):
    titulo(f'Acessando o manual do comando \'{comando}\'', 4)
    print(cores[6], end='')
    help(comando)
    print(cores[0], end='')
    sleep(1.5)


def titulo(mensagem, cor=0):
    tamanho = len(mensagem) + 4
    print(cores[cor], end='')
    print('-' * tamanho)
    print(f'    {mensagem}')
    print('-' * tamanho)
    print(cores[0], end='')
    sleep(0.8)


#Programa Principal

escolha_comando = ''
while True:
    titulo('SISTEMA DE AJUDA E ORIENTAÇÃO PyHELP', 2)
    escolha_comando = str(input('Escolha uma Função ou Biblioteca para obter mais informações ->: '))
    if escolha_comando.upper() == 'FIM':
        break
    else:
        ajuda(escolha_comando)
titulo('Até Logo!!', 1)