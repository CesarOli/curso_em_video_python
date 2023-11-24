from time import sleep
print('\033[1;31mAnalisando Triângulo v2.0\033[m\n')
print('Informe o valor de três retas, afim de saber se consigo ou NÃO formar um triângulo: \n')
r1 = float(input('valor da primeira reta: '))
r2 = float(input('valor da segunda reta: '))
r3 = float(input('valor da terceira reta: '))
print('PROCESSANDO...')
sleep(1.5)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Sim, é possível formar um triângulo.')
    if r1 == r2 and r1 == r3 and r2 == r3:
        print('Este triângulo é um triângulo EQUILÁTERO, ou seja, possue todos os lados com a mesma medida.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Este triângulo é um triângulo ISÓSCELES, pois possuem dois lados com a mesma medida.')
    else:
        print('Este triângulo é um triângilo ESCALENO, ou seja, possuem todos os lados com medidas diferentes.')
else:
    print('Não é possível formar um triângulo.')