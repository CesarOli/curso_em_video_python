# Faça um progrma que leia nome e média de um aluno
# e guarde também a situação, tudo em um dicionário'{}'
# Ao final, mostre o conteudo da estrutura na tela.

aluno = {}
aluno['Nome'] = str(input('Nome: '))
aluno['Media'] = float(input('Informe sua média: '))
if aluno['Media'] <= 7.00:
    aluno['Situacao'] = 'Reprovado'
else:
    aluno['Situacao'] = 'Aprovado'

for k, v in aluno.items():
    print(f'{k} é igual a {v}')
