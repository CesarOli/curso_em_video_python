import string
frase = str(input('Me diga aí, qualquer coisa, qualquer coisa msm: ')).lower().strip()
print('Sua frase contém {} letras "a".'.format(frase.count('a')))
print('A primeira letra "a" aparece na posição {}'.format(frase.find('a')))
print('A última letra "a" aparece na posição {}'.format(frase.rfind('a')))
print(frase)

