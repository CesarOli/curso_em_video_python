from time import sleep
palavras = ('amor', 'COMIDA','futebol', 
            'MARGARINA', 'agua', 'SACOLA',
             'terminal', 'ABAJOUR', 'caixa de som',
             'FONTE', 'televisao', 'TOALHA', 'hamburguer', 
             'PROGRAMAR', 'estudar', 'BEIJAR',
             'curtir','FOCAR', 'relaxar')

vogais = 'aeiouAEIOU'

for palavra in palavras:
    vogais_achadas = []

    for letra in palavra:
        if letra in vogais: 
            vogais_achadas.append(letra)

    if vogais_achadas:
        vogais_novas = ', '.join(vogais_achadas)
        sleep(0.4)
        print(f'Vogais em "{palavra}": {vogais_novas}')
    else:
        print(f'Não encontrei vogais nesta "{palavra}" ')
    resposta = ' '
    '''while resposta not in 'SN':
        resposta = str(input('Deseja continuar "S" ou "N"?: ')).strip().upper()[0]
        if resposta == 'N':
            break'''
print('Fim do Programa!!')