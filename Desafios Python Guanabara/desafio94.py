#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os 
#dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
#No final, mostre: 
# - quantas pessoas foram cadastradas 
# - A média de idade do grupo
# - Uma lista com todas as mulheres 
# - Uma lista com a todas as pessoas com idade acima da média 

'''pessoa = {}
cadastro = []
media = 0


while True:
    pessoa['Nome'] = str(input('Digite aqui o seu nome: '))

    pessoa ['sexo'] = str(input('Digite aqui seu sexo, "F" ou "M": ' )).upper().strip()

    while True:
        pessoa['sexo'] = input('Digite aqui seu sexo, "F" ou "M": ').upper().strip()
        
        if pessoa['sexo'] not in 'M' or 'F':
            break
        else:
            print('Por favor, digite somente "F" ou "M".')

    pessoa['idade'] = int(input('Digite sua idade: '))
    cadastro.append(pessoa.copy())
    resposta = str(input('Deseja continuar: S/N: ')).strip().upper()
    if resposta == 'N':
        break
media = media + pessoa['idade'] / len(cadastro)
print(media)

print(f"No total foram cadastradas {len(cadastro)} pessoas.")'''

pessoas = []
soma_idades = 0

while True:
    pessoa = {}
    pessoa['nome'] = input('Digite o nome da pessoa (ou "sair" para encerrar): ')
    
    if pessoa['nome'].lower() == 'sair':
        break
    
    pessoa['sexo'] = input('Digite o sexo da pessoa (M/F): ')
    pessoa['idade'] = int(input('Digite a idade da pessoa: '))
    
    pessoas.append(pessoa)
    soma_idades += pessoa['idade']

quantidade_pessoas = len(pessoas)
media_idade = soma_idades / quantidade_pessoas if quantidade_pessoas > 0 else 0

mulheres = [pessoa['nome'] for pessoa in pessoas if pessoa['sexo'].lower() == 'f']
acima_media = [pessoa for pessoa in pessoas if pessoa['idade'] > media_idade]

print(f'\nQuantidade de pessoas cadastradas: {quantidade_pessoas}')
print(f'Média de idade do grupo: {media_idade:.2f}')
print(f'Lista de mulheres: {mulheres}')
print(f'Pessoas com idade acima da média: {[pessoa["nome"] for pessoa in acima_media]}')
