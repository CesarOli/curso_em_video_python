print('\033[1;31mMaior e Menor da Sequência.\033[m')
maior = 0
menor = 0
for medida in range(1, 62):
    peso = float(input('Me diga qual o seu peso em Kg: '))
    if medida == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é {}Kg'.format(maior))
print('A mais leve aqui tem {:.0f}Kg.'.format(menor))