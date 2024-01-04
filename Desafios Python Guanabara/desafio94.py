#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os 
#dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
#No final, mostre: 
# - quantas pessoas foram cadastradas 
# - A média de idade do grupo
# - Uma lista com todas as mulheres 
# - Uma lista com a todas as pessoas com idade acima da média 

pessoa = {}
cadastro = []
media = soma = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Digite seu nome: '))

    while True:
        pessoa['sexo'] = str(input('Digite seu sexo (M/F): ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO: Por favor, digite somente M ou F: ')
    pessoa ['idade'] = int(input('Digite sua idade: '))
    soma += pessoa['idade']
    cadastro.append(pessoa.copy())
    while True:
        resposta = str(input('Deseja encerrar o programa? [S/N]')).upper()[0]
        if resposta in 'SN':
            break
        print('ERRO!! Responda apenas S ou N.')
    if resposta == 'S':
        break
     
print(cadastro)
print(f'Ao todo temos {len(cadastro)} pessoas cadastradas.')
media = soma / len(cadastro)
print(f'A média de idade é de {media:5.2f} anos.')
print('As mulheres cadastradas foram ', end='')
for p in cadastro:
    if p['sexo']in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('Lista das pessoas que estão acima da média: ')
for p in cadastro:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< PROGRAMA ENCERRADO!!')
