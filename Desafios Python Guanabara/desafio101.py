# Crie um programa que tenha uma função chamada voto() que vai receber como 
# parâmetro o ano de nascimento de uma pessoa, retornando um valor literal 
# indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.

def voto(ano_nascimento):
    from datetime import datetime
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    if idade < 16:
        return 'NEGADO!'`
    elif 16 <= idade < 18 or idade >= 70:
        return 'OPCIONAL'
    else:
        return 'OBRIGATÓRIO'
    

ano_nascimento = int(input('Informe o seu ano de nascimento: '))
resultado_voto = voto(ano_nascimento)
print(f'Seu voto é {resultado_voto} nas próximas eleições.')
