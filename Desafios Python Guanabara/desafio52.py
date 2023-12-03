print('\033[1;31mNúmeros Primos.\033[m')
n = int(input('Digite um número para saber se ele é um número primo ou não: '))
mult = 0
for c in range(2, n):
    if n % c == 0:
        mult += 1
if mult == 0:
    print('é primo!!')
else:
    print('não é primo.')
