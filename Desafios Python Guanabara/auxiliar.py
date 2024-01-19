'''frase = str('Curso em Vídeo Python').strip()
print(len(frase))
print(frase[9])
print(frase[9:13])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])
print(len(frase))
print(frase.count('o'))
print(frase.count('o', 0, 13))
print(frase.find('deo'))
print(frase.find('Carine'))
print('Vídeo' in frase)
frase = frase.replace('Python', 'Android')
print(frase)
print(len(frase))
frase = frase.replace('Android', 'Python')
print(frase)
print(len(frase))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
novafrase = '   Aprenda Python   '
print(novafrase)
print(novafrase.strip())
print(novafrase.rstrip())
print(novafrase.lstrip())
print(frase)
print(frase.split())
print('.'.join(frase[::]))

print(frase)
print(frase[0:21:2])
print(frase)
print(frase.upper().count('c'))
print(frase.lower().count('o'))
print(frase.split())
dividido = frase.split()
print((dividido[0]))
print(dividido[2][3])
tempo = int(input('Há quantos anos você tem seu carro? '))
if tempo <=3:
    print('Hmm q boy, tem carro novo.')
else:
    print('Ecaa, q carro véio tiw!! Ahahaha')
print('---FIM!!---')

print('\nCondição Simplificada: em uma linha de código.\n')
tempo = int(input('Há quantos anos você tem seu carro? '))
print('Hmm q boy, anda de carro novo.'if tempo <=3 else' tá ruim pra vc hein tiw, que carro velho!!')
print('---FIM---')

print('\nCondicional Simples, sem desvio.\n')
nome = str(input('Qual é seu nome? ')).strip()
if nome == 'César' or 'Carine' or "Tereza":
    print('Que nome lindo você tem!!')
print('Bom dia, {}' .format(nome))
print('---FIM---')

print('\nCondicional Composta.\n')
nota1 = float(input('Digite aqui o valor da sua primeira nota na AV1: '))
nota2 = float(input('Digite aqui o valor da sua segunda nota na AV2: '))
m = (nota1 + nota2)/2
print('Sua média foi {}'.format(m))
if m >= 7:
    print('Eu sabia, você tá de Parabéééns :D!!')
else:
    print('Você é fooogo hein, vai precisar estudar mais...Seu Saroba!!')
print('---FIM---')

print('\nCondicional Simplificada!\n')
nota1 = int((input('Digite aqui a sua primeira nota: ')))
nota2 = int(input('Digite aqui a sua segunda nota: '))
m = (nota1 + nota2)/2
print('Sua média foi {}'.format(m))
print('Parabéns, eu sabia q vc era desses.' if m>=7 else 'Vc é um Sarobão msm hein. Estuda mais.')
print('---FIM!!---')

print('\033[4;33mCondições Aninhadas: If, Elif, Else.\033[m\n')

nome = str(input('Qual o seu nome? ')).strip()
if nome == 'César':
    print('Que nome Lindo!!')
elif nome == 'Samuca' or nome == 'Arthur':
    print('Eu lembro de vc o tempo todo, lindão.')
elif nome == 'Tereza':
    print('Eu penso na Sra. o dia todo mamãezinha!!')
elif nome == 'Carine':
    print('Eu penso em vc o tempo todo.')
elif nome in 'Julia, Gal, Sandra, Débora, Suellen, Fernanda.':
    print('to suave de vc...')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!!'.format(nome))

print('\n\033[1;34mEstrutura de Repetição\033[m, \033[1:37mFOR.\033[m')
for c in range(1, 6):
    print(c)
print('\nFIM')
for x in range(6, 0, -1):
    print(x)
print('FIM')

for y in range(6, 0, -2):
    print(y)
print('FIM')

numero = int(input('Digite um numero: '))
for c in range(0, numero):
    print(c)

i = int(input('Um número para iniciar: '))
f = int(input('Um número para finalizar: '))
p = int(input('quantos passos deseja dá: '))
for c in range(1, f+1, p):
    print(c)

s = 0
for c in range(0, 4):
    numero = float(input('Digite um valor: '))
    s += numero
print('A somatória de todos os valores é {:.0f}.'.format(s))
print('FIM')

print('\n\033[1;34mEstrutura de Repetição\033[m, \033[1:37mFOR.\033[m')
for c in range(1, 6):
    print(c)
print('\nFIM')
for x in range(6, 0, -1):
    print(x)
print('FIM')

for y in range(6, 0, -2):
    print(y)
print('FIM')

numero = int(input('Digite um numero: '))
for c in range(0, numero):
    print(c)

i = int(input('Um número para iniciar: '))
f = int(input('Um número para finalizar: '))
p = int(input('quantos passos deseja dá: '))
for c in range(1, f+1, p):
    print(c)
s = 0
for c in range(0, 4):
    numero = float(input('Digite um valor: '))
    s += numero
print('A somatória de todos os valores é {:.0f}.'.format(s))
print('FIM')
for cesar in range(1, 10):
    print(cesar)
elas = ['Fernanda', 'Carine', 'Gal', 'Júlia', 'Cintia', 'Sandra']
for ela in elas:
    print(ela)
print('\033[1;7;33mFeira da Semana.\033[m')
frutas = ['banana', 'maçã', 'abacate', 'limão', 'abacate', 'laranja', 'mamão', 'manga']
print(frutas)
for fruta in frutas:
    print(fruta)
print(len(frutas))
print(frutas.count('limão'))
for aluno in ['Thiago', 'Lebin', 'Isa', 'Rafa', 'Má']:
    print(aluno)

frase = 'Capoeira, é jogo de mandinga, vamo vadia'
for capoeira in frase:
    print(capoeira[])
n = int(input('Digite um numero: '))
for c in range(0, n+1):
    print(c)
print('FIM')
for carine in range(0, 3):
    n = int(input('Digite um valor: '))
    s = s + n
print('O somatório dos números é igual a {}.'.format(s))
i = int(input('Digite o início: '))
f = int(input('Digite o fim: '))
p = int(input('Em qtos passos: '))
for c in range(i, f, p):
    print(c)
print('FIM')
s = 0
print('Estudando Laço de Repetição \033[2;32m"While".\033[m')
for c in range (1, 10):
    print(c)
print('FIM')
c = 1
while c < 10:
    print(c)
    c += 1
print('FIM')
for c in range(1, 5):
    n = int(input('Digite um valor: '))
print('FIM')
n = 8
while n != 0:
    n = int(input('Digite um valor: '))
print('FIM')
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Deseja continuar [S/N] ')).upper()
print('FIM')
n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} impares.'.format(par, impar))
print('Acabou')

for c in range(1, 3):
    n = int(input('Digite um valor: '))
print('Fim')

c = 1
while c < 10:
    print(c)
    c = c + 1
print("FIM")
r = 'S'
n = 1
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]: ')).upper()
print('FIM')

n = 1
c = 0
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('A quantidade de números pares é de {}.'.format(par))
print('...e a quantidade de números impares foi de {}.'.format(impar))
print('Fechoou!!')
i = 1
while i <= 6:
    print(i)
    i += 1
print('\n')
i = 10
while i <= 100:
    print(i)
    if i == 30:
        break
    i = i + 10
i = 0
while i < 6:
    i += 1
    if i == 3:
        break
        print(i)
cont = 1
while cont < 11:
    print(cont, ' - ', end='')
    cont += 1
print('Acabou!!')
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
#print('A soma vale {}.'.format(s))
print(f'A soma vale {s}')
nome = ''
n1 = 2
n2 = -25
media = 2.5
nome = 'César Alexandre Oliveira'
logado = True
print(100)
print('Carine, você sim é bem Goooostosa.')
print(nome, 'te curte, aquele idiota!! Ahahahha.')
input(nome)
a = 4
b = 98
c = 12
resultado = True
print(a < b)
print(a != b)
resultado = a != (b + c)
print(resultado)

a = 5
b = 7
res = (a + b) / 2
print(res)
print('CALCULADORA SIMPLES')
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um segundo número: '))
print('\nRESULTADO')
res = n1 + n2
print(n1, ' +', n2, ' =', res)
res = n1 - n2
print(n1, ' -', n2, ' =', res)
res = n1 * n2
print(n1, ' x', n2, ' =', res)
res = n1 / n2
print(n1, ' /', n2, ' =', res)
res = n1 % n2
print(n1, ' %', n2, ' =', res) #resto da divisão
res = n1 ** n2
print(n1, ' ^', n2, ' =', res)
res = n1 // n2
print(n1, ' //', n2, ' =', n2)

f = int(input('Digite a temperatura em Fahrenhei: '))
c = (f - 32) / 1.8
print('Celsius: {:.1f}°C.'.format(c))
k = c + 273
print('Kelvin: {:.1f}.'.format(k))
print('FIM!!')

cont = 1
while cont <= 11:
    print(cont, ' -> ', end='')
    cont += 1
print('Acabou!\n')

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s = s + n
print('A soma vale {}'.format(s))
# fstrings
print(f'A soma vale {s}')
nome = 'César'
idade = 40
ela = 'Carine'
print(f'O lindão do {nome}, quer pega vc {ela}, ele ainda guenta, tem só {idade} anos, ta novin o negão...')

a = int(input())
b = int(input())

X = a + b

print(f'X = {X}')
r = int(input('Digite o valor da área que deseja calcular: '))
n = float(3.14159)
A = n * (r**2)

print('{:.4f}'.format(A))

r = float(input())
n = float(3.14159)
A = n * (r**2)

print('A={:.4f}'.format(A))

a = int(input())
b = int(input())
soma = a + b

print(f'SOMA = {soma}')

x = int(input())
y = int(input())

PROD = x * y
print(f'PROD = {PROD}

A = float(input()) * 3.5
B = float(input()) * 7.5

MEDIA = (A + B) / 11
print('MEDIA = {:.5F}'.format(MEDIA))

#Leia 3 valores, no caso, variáveis A, B e C, que são as três notas de um aluno.
# A seguir, calcule a média do aluno, sabendo que a nota A tem peso 2, a nota B tem peso 3 e a nota C tem peso 5.
# Considere que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.

A = float(input()) * 2
B = float(input()) * 3
C = float(input()) * 5

MEDIA = (A + B + C) / 10

print('MEDIA = {:.1f}'.format(MEDIA))

#Leia quatro valores inteiros A, B, C e D.
# A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula:
# DIFERENCA = (A * B - C * D).
#Entrada
#O arquivo de entrada contém 4 valores inteiros.
#Saída
#Imprima a mensagem DIFERENCA com todas as letras maiúsculas,
# conforme exemplo abaixo, com um espaço em branco antes e depois da igualdade.


A = int(input())
B = int(input())
C = int(input())
D = int(input())
print(A, B, C, D)

DIFERENCA= (A * B - C * D)
print('DIFERENCA = {}'.format(DIFERENCA))

#Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas,
#o valor que recebe por hora e calcula o salário desse funcionário. A seguir,
#mostre o número e o salário do funcionário, com duas casas decimais

n = int(input())
h = int(input())
v = float(input())
salary = h * v
print('NUMBER = {}'.format(n))
print('SALARY = U$ {:.2f}'.format(salary))

n = str(input())
s = float(input())
d = float(input())
c = d * 15/100
t = s + c
print('TOTAL  = R$ {:.2f}'.format(t))

Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1,
o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.
Entrada
O arquivo de entrada contém duas linhas de dados. Em cada linha haverá 3 valores, respectivamente dois inteiros
e um valor com 2 casas decimais.
Saída
A saída deverá ser uma mensagem conforme o exemplo fornecido abaixo, lembrando de deixar um espaço após
os dois pontos e um espaço após o "R$". O valor deverá ser apresentado com 2 casas após o ponto.
primeiraLinha = input().split()
segundaLinha = input().split()
codigoPeca1 = quantidadePeca1 = valorPeca1 = primeiraLinha
codigoPeca2 = quantidadePeca2 = valorPeca2 = segundaLinha

print(primeiraLinha)
print(segundaLinha)

total = int(quantidadePeca1) * (float(valorPeca1)) + int(quantidadePeca2) * (float(valorPeca2))
print(total)

print('Hello Word')

ela = "carine"
print(ela)
from time import sleep
lanche = 'hamburguer'
lanche = 'Suco'
#TUPLAS SÃO IMUTÁVEIS
#lanche[3] = 'VC'
lanche = ('Ovo', 'Frango', 'Abacaxi', 'Linão', 'Mamão', 'VC')

#/for comida in lanche:
#    sleep(0.5)
#    print(f'Eu vou comer {comida}')
#    sleep(0.5)
#print(lanche[1])
#for c in range(0, len(lanche)):
#    sleep(0.5)
#    print(f'Eu vo comer {lanche[c]} na posição {c}')
#    sleep(1)
#for pos, comida in enumerate(lanche):
#    sleep(0.5)
#    print(f'Vo come muito {comida} na posição {pos}')
#    sleep(0.5)
#sleep(1)
#print('Comi demais!!')
#sleep(2)
#print('Comi', len(lanche), 'lanches no final da festa. \nTo Cheião!!')

#print(lanche)
#print(sorted(lanche))

#a = (2, 5, 4)
#b = (5, 8, 1, 2)
#c = b + a
#print(a)
#print(b)
#print(c)
#print(sorted(c))
#print(len(c))
#print(c.count(5))
#print(c.index(5, 1))

pessoa = ('César', 40, 'M', 89.44)
print(pessoa)
del(pessoa[1])
del linha():
    print(==========)


linha():

# Tuplas
janta = ('Mandioca', 'Arroz', 'Feijao', 'Ovo', 'Frango')

#Listas
lanche = ['Aveia', 'Banana', 'Agua', 'Limao', 'Abacaxi']

print('Janta -> ', janta)
print('Lanche -> ', lanche)

print(lanche[2])
print(janta[2])

lanche.append('Cenoura') # adiciona elementos ao final da lista
lanche[0]= 'Carne Moída'
lanche.insert(0,'Agrião') # adiciona novo elementos na pósição que eu determinar.
lanche.append('Bolo de Cenoura')
lanche.append('Refrigerante')
lanche.append('Chocolate Branco')
print(lanche)

del lanche[7]
lanche.pop()
if 'Refrigerante' in lanche:
    lanche.remove('Refrigerante')
else: 
    print('Não existe este item nesta lista')

print('Janta -> ', janta)
print('Lanche -> ', lanche)


numeros = list(range(1, 12))
numeros.sort(reverse=True)
print(len(numeros))


valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v}...')

for c, v in enumerate(valores):
    print(f'Na posição {c}, encontrei o valor {v}!')

valores = []
for contador in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

print(valores)

for contador, v in enumerate(valores):
    print(f'Na posição {contador} encontrei o valor {v}')

print('Fim do programa!')

a = [2, 3, 4, 7]
b = a 
b = a[:] # cria uma cópia da lista 'a' em 'b'
b[2]= 8 #substituo a posição 2 pelo número 8 nas duas listas, pois isso é ligação
        #entre as listas
print(f'lista a {a}')

a.append(10)
print(f'\nlista {a}')
'''

# Listas Compostas

'''
elas = list()
elas.append('Carine')
elas.append(20)
todas = list()
todas.append(elas[:])
elas[0] = 'Larissa'
elas[1] = 22
todas.append(elas[:])
print(todas)

dados = list()
dados.append('César')
#print(dados)
#print(len(dados))

dados.append(40)
#print(dados)
#print(len(dados))

dados.append('trampo')
#print(dados)
#print(len(dados))

#print(dados[0])
#print(dados[1])
#print(dados)


pessoas = list()
pessoas.append(dados[:])
pessoas = [['Pedro', 25],['Maria', 19],['João', 32]]
print(pessoas)
print(pessoas[0])
print(pessoas[1])
print(pessoas[2])
print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][0])

print(pessoas[1])


teste = list()
teste.append('César')
teste.append(40)
print(teste)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])

galera = [['Joao', 19],['Ana', 33],['Joaquim', 13],['Maria', 45]]
for pessoa in galera:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')


galera = list()
dado = list()
totmai = totmen = 0

for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.' )

pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][0])
print(pessoas[1])

teste = []
teste.append('César')
teste.append(40)
galera = []
galera.append(teste[:])
teste[0] = 'Carine'
teste[1] = 20
galera.append(teste[:])
print(galera)


turma = [['João', 52], ['Carlota', 15],
         ['Josefina', 23], ['Pedrita', 32]]
for troxa in turma:
    print(f'O nome é {troxa[0]}, e a idade é {troxa[1]}.')

elas = []
temp = []
for mina in range(3,3):
    temp.append(str(input('Seu nome: ')))
    temp.append(int(input('Sua idade: ')))
    elas.append(temp[:])
    temp.clear()

for gostosa in elas:
    if gostosa[1] >= 21:
        print(f'{gostosa[0]} nem vem que vc aguenta sim, até pq sua idade é de {gostosa[1]} anos.')
print(elas)

pessoas = {'nome': 'César','sexo': 'M', 'idade': 40}
print(pessoas)
print(pessoas['idade'])
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
#del pessoas['sexo']
pessoas['nome'] = 'Arthur'
pessoas['peso'] = 54.4
for k, v in pessoas.items():
    print(k, v)

brasil = []
estado1 = {'uf':'Rio de Janeiro' ,'sigla': 'RJ'}
estado2 = {'uf':'São Paulo' ,'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(estado1)
print(estado2)
print(brasil)
print(brasil[0])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])


estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')


num = [2, 5, 9, 1]
num[2] = 3
num.append(15)
num.sort(reverse=True)
num.insert(2, 2)
print(num)
print(f'Essa lista tem {len(num)} elementos.')
if 5 in num:
    num.remove(5)
else:
    print('Não achei este número na lista.')


valores = []
valores.append(5)
valores.append(9)
valores.append(4)
print(valores)


for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao fina da lista.')


valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!!')
print('Cheguei ao final da lista.')

a = [13, 8, 23, 24]
b = a[:]
b[2]= 8
print(f'Lista A = {a}.')
print(f'Lista B = {b}.')

teste = []
teste.append('César')
teste.append(40)
galera = []
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]

for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')


galera = []
dado = []
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade:')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else: 
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores de idade e {totmen} menores de idade.')

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for posicao, v in enumerate(valores):
    print(f'na posição {posicao} encontrei o valor {v}')
print('Cheguei ao final da lista')

#Dicionários


dados = {}
dados = dict()

dados = {'nome': 'Pedro', 'idade': 25}

print(dados)
print(dados['nome'])
print(dados['idade'])
dados['sexo'] = 'M'
print(dados)
del dados['idade']
print(dados)

filmes = {'título':'Star Wars',
          'ano': 1977,
          'diretor': 'George Lucas' 
}
print(filmes)
print(filmes.values())
print(filmes.keys())
print(filmes.items())

for k, v in filmes.items():
    print(f'O {k} é {v}')

pessoas = {'nome':'César', 'sexo': 'M', 'idade': 41}
print(pessoas.values())
print(pessoas.keys())
print(pessoas.items())

del pessoas['sexo']
pessoas['nome'] = 'Carlota'
pessoas['peso'] = 90.2
for k, v in pessoas.items():
    print(f'{k} = {v}')

#Dicionários dentro de uma lista

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf':'São Paulo', 'sigla': 'SP'}

brasil.append(estado1)
brasil.append(estado2)

print(brasil[1]['uf'])


estado = {}
brasil = []
for c in range (0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
for estado in brasil:
    for k, v in estado.items():
        print(f'O campo {k} tem valor {v}')


pessoas = {'nome': 'César', 'sexo':'M', 'idade':41}
print(pessoas)

for v in pessoas.values():
    print(f'{v}')
    
#Funções
#Comandos def

def mostra_linha():
    print('---' * 10)

#Programa Principal

mostra_linha()
print('    Curso Em Vídeo    ')
mostra_linha()
print('    Aprenda Python     ')
mostra_linha()
print('    César Oliveira    ')
mostra_linha()


def titulo(txt):
    print(txt)
    print('---' * 10)
    


#Programa Principal

titulo('    Curso Em Vídeo    ')
titulo('    Aprenda Python     ')
titulo('    César Oliveira    ')


a = 4 
b = 5 
s = a + b 
print(s)

a = 8
b = 9 
s = a + b
print(s)

a = 2 
b = 1
s = a + b  
print (s)



def soma(a, b):
    s = a + b 
    print(s)


soma(4, 5)
soma(9, 8)
soma(2, 1)'''

def soma(a, b):
    print(f'A = {a} e B = {b} ')
    s = a + b
    print(f'A soma A + B = {s}')

# Programa Principal
soma(1, 4)
soma(b=3, a=54)