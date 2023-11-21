print('\033[1;31mMaior e Menor valor.\033[m'
      '')
print('Para saber qual número é maior, digite três números.\n')
n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
n3 = int(input('Informe o terceiro número: '))
maior = n1
if (n2 > maior):
    maior = n2
if (n3 > maior):
    maior = n3
print('o maior valor digitado foi {};'.format(maior))
menor = n1
if(n2 < menor):
    menor = n2
if(n3 < menor):
    menor = n3
print('o menor valor digitado foi {}.'.format(menor))

print('\n---fim---')
