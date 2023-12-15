from time import sleep

#Crie uma tupla preenchida com os 20 primeiros 
# colocados da Tabela do Campeonato Brasileiro 
# de Futebol na ordem da colocaçao. 
# Depois mostre:
#A) Apenas os 5 primeiros:
#B) Os 4 últimos colocados da tabela:
#C) Uma lista com os times em ordem alfabética:
#D) em que posição está o seu time na tabela:

tabela_brasileirao_2023 = ('Botafogo', 'Flamengo', 'Fluminense', 'Palmeiras', 'Grêmio', 
                      'Athletico-PR', 'Bragantino', 'São Paulo', 'Cuiabá', 'Internacional', 
                      'Cruzeiro', 'Fortaleza', 'Atlético MG', 'Corinthians', 'Góias', 'Santos', 
                      'Bahia', 'Coritiba', 'América-MG', 'Vasco da Gama')
c = 0
#print(tabela_brasileirao_2023)
for clube in tabela_brasileirao_2023:
    sleep(1)
    c =+ 1
    print(c, '-', clube)


#print(tabela_brasileirao_2023[0:5])
#print(tabela_brasileirao_2023[-4:])
#print(sorted(tabela_brasileirao_2023))
'''while True:
    time_digitado = input('Digite o time para descobrir a posição dele na tabela do brasileirão 2023: ')

    try:
        time_posicao = tabela_brasileirao_2023.index(time_digitado) + 1
        print(f'O {time_digitado} está na {time_posicao}ª posição na tabela.')
        break
    except ValueError:
        print(f'O {time_digitado} não está na tabela.')'''
sleep(0.5)
print('Fim do Programa!!')