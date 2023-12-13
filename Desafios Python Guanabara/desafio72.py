from time import sleep
#Crie um programa que tenha uma tupla totalmente
#prenchida com uma contagem por extenso de zero a vinte.
#O programa deverá ler um número pelo teclado(entre 0 e 20)
#e mostrá-lo por extenso.

numeros_por_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
                       'seis', 'sete', 'oito', 'nove', 'dez', 
                       'onze', 'doze', 'treze', 'catorze', 'quinze', 
                       'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True: 
    try:
        sleep(0.10)
        numero_digitado = int(input('digite um numero entre 0 e 20: '))
        if 0 <= numero_digitado <= 20:
            break
        else:
            sleep(0.10)
            print('Número digitado está fora do intervalo solicitado.')
    except:
        sleep(0.10)
        print('Número inválido, informe números entre 0 e 20. Obrigado!!')
sleep(1)
print(f'Você digitou o número, {numeros_por_extenso[numero_digitado]}.')
resposta = input('Deseja continuar digitando números e vendo por extenso: ')
if resposta == 'Ss':
    
sleep(0.5)
print('Fim do Programa!!')
    