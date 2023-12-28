from time import sleep

# Crie um programa que leia nome e duas notas de vários alunos e guarde
# em uma lista composta.
# Ao final, mostre um boletim contendo a média de cada um 
#e permita que o usuário possa mostrar as notas de cada aluno individualmente.

nome_alunos_e_notas = []
nota_um = 0
novo_aluno = ''
while novo_aluno != 'N':
    nome = str(input('Digite seu nome: '))

    while True:
        nota_um = float(input('Digite a nota da sua primeira prova: '))
        nota_dois = float(input('Digite a nota da sua segunda prova: '))
        if nota_um > 10 or nota_dois > 10:
            print('Digite uma nota válida (0 a 10), por favor!')
        else:
            break
    media = (nota_um + nota_dois) / 2

    nome_alunos_e_notas.append([nome, [nota_um, nota_dois], media])
    print(nome_alunos_e_notas)
    novo_aluno = str(input('Deseja incluir um novo aluno: S/N: '))
    if novo_aluno == 'n' or novo_aluno == 'N':
        break

print()
print(f'{"Nº.":<4}{"NOME":<10}{"MÉDIA":>8}')
print()

for i, aluno in enumerate(nome_alunos_e_notas):
    print(f'{i:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')

while True:
    print()
    opcao = int(input('Deseja mostrar as notas de qual aluno? (A opção 999 interrompe o programa!: '))
    if opcao == 999:
        print('Encerrando programa!')
        sleep(1.5)
        break
    if opcao <= len(nome_alunos_e_notas) - 1:
        print(f'Notas de {nome_alunos_e_notas[opcao][0]} foram {nome_alunos_e_notas[opcao][1]}')
print('Fim do Programa!!')