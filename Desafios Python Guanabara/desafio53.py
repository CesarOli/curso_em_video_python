'''print('\033[1;31mDetector de Palíndromo\033[m')
frase = str(input('Diga uma frase qualquer para detectar se é ou não um PALÍNDROMO: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('A frase \033[32m{}\033[m é Palíndromo.'.format(frase))
else:
    print('Está frase \033[33m{}\033[m não é um Palíndromo.'.format(frase))'''

print('\033[32mSegunda forma de fazer, sem utilizar o "FOR".\033[m')
print('\033[1;31mDetector de Palíndromo.\033[m')
frase = str(input('Digite a frase que deseja saber se é um Palíndromo ou não: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
if junto == inverso:
    print('A frase {} é um Palíndromo.'.format(frase))
else:
    print('A frase {} não é uma Palíndromo.'.format(frase))
