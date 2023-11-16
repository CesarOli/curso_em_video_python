print('\nChamando a Biblioteca inteira (Matemática)')
import math
angulo = float(input('\nInforme um ângulo qualquer: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O ângulo {} tem o SENO de {:.2f}'.format(angulo, seno))
print('O ângulo {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
print('O ângulo {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))


'''print('\nChamando somente o que usarei da biblioteca (Matemática)')
from math import sin, cos, tan, radians

angulo = float(input('\nInforme o ângulo que deseja consultar seu SENO, COSSENO e TANGENTE: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O ângulo {} tem o SENO de {:.2f}'.format(angulo,seno))
print('O ângulo {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
print('O ângulo {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))'''