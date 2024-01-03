from datetime import datetime

#Crie um programa que leia o 'nome','ano de nascimento' e 'carteira de trabalho
#Cadastre-os (com idade) em um dicionário, se por acaso o CTPS(carteira de trabalho) 
#for diferente de 0, o dicionário receberá também o ano de contratação e o salário
#Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

cadastro = {}

cadastro['nome'] = str(input('Qual é o seu nome: '))
cadastro['ano_nascimento'] = int(input('Ano Nascimento: '))
ano_atual = datetime.now().year
idade = ano_atual - cadastro['ano_nascimento']
cadastro['idade'] = idade
del cadastro['ano_nascimento']
cadastro['carteira_de_trabalho'] = int(input('Informe o número da sua carteira de trabalho (CTPS) (0 não tem carteira): '))

if cadastro['carteira_de_trabalho'] != 0:
    cadastro['ano_contratacao'] = int(input('Informe o ano de contratação: '))
    cadastro['salario'] = float(input('Informe seu salário: R$ '))
    cadastro['aposentadoria'] = cadastro['idade'] + ((cadastro['ano_contratacao'] + 35) - ano_atual) 
for k, v in cadastro.items():
    print(f'- {k} tem o valor {v}')

print('Fim do Programa!')
