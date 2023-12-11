print('\033[1;31mSuper Progresssão Aritmetica.\033[m')
pt = int(input('Informe o primeiro termo da PA que deseja saber: '))
razao = int(input('Informe a razao da PA que deseja saber: '))
contador = 1
termo = pt
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print('{} -> '. format(termo), end='')
        termo = termo + razao
        contador = contador + 1
    print('Pausa Dramática...rsrs')
    mais = int(input('Qtos termos vc deseja mostrar a mais: '))
print('Progressão Finaliza com {} termos mostrados.'.format(total))

