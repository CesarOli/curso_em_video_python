# Faça um programa que tenha uma função chamada contador(), que receba três 
# parâmetros: início, fim, passo e realize a contagem. 
# O programa deve realizar três contagens através da função criada: 

# De 1 a 10, de 1 em 1.
# De 10 a 0, de 2 em 2.
# Uma contagem personalizada.


from time import sleep


def contador(inicio, fim, passo):

    if passo < 0:
       passo *= -1
    if passo == 0:
        passo = 1
    
    print(f'\nContagem de {inicio} até {fim} de {passo} em {passo}.') 
    sleep(2.5)

    if inicio < fim:
        c = inicio
        while c <= fim:
            print(c, end=' ', flush=True)
            sleep(0.5)
            c += passo
        print('FIM!!\n')
    else:
        c = inicio
        while c >= fim:
            print(f'{c} ', end='', flush=True)
            sleep(0.5)
            c -= passo
        print('FIM!!')


#Programa Principal
contador(0, 100, 10)
contador(10, 0, 2)
sleep(1)
print("Informe e monte como gostaria de ver seu contador: ")
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)


