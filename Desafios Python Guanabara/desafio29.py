from time import sleep
print('VELOCIDADE DO CARRO\n')
velocidade = float(input('Qual a velocidade que seu carro está marcando neste exato momento? '))
print('PROCESSANDO...')
sleep(2)
if velocidade <= 80:
    print('Ok, pode seguir viagem, obrigado!!')
else:
    multa = (velocidade - 80) * 7
    print('Parabéééns manéé, você foi multado em R${} reais.'.format(multa))
print('Sua velocidade real foi de {}KM.'.format(velocidade))
print('\n---FIM---')