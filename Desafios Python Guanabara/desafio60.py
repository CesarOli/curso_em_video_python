from math import factorial
print('\033[1;31mCálculo Fatorial.\033[m')
'''n = int(input('Informe um número para saber o seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))


n = int(input('Informe um número para saber seu fatorial: '))
c = n
resultado = 1
while c > 0:
    print('{} '.format(c), end='')
    print('x ' if c > 1 else ' = ', end='')
    resultado *= c
    c = c - 1
print('{}'.format(resultado))'''

n = int(input("Informe um número para saber seu fatorial: "))
f = n
for f in range(n > 0):
    f = factorial(n)
print('{}'.format(f))

'''n = int(input('Informe um número para saber seu fatorial: '))
f = n
c = 1
resultado = 1
for fatorial in range(n > 0):
    print('{}'.format(f), end='')
    print('x' if c > 1 else ' = ', end='')
    f *= 1
    c -= 1
print('{}'.format(resultado))
'''