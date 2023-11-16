'''from math import sqrt, hypot
x = float(input('Informe o valor do cateto oposto da hipotenusa: '))
y = float(input('Informe o valor do cateto adjacente da hipotenusa: '))
z = hypot(x, y)
print('A hipotenusa é {:.2f} '.format(z))'''
import math

import math
x = float(input('informe o valor do cateto oposto da hipotenusa: '))
y = float(input('informe o valor do cateto adjacente da hipotenusa: '))
z = math.hypot(x, y)
print('a hipotenusa é {:.2f}'.format(z))