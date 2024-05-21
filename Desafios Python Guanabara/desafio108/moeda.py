# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
# diminuir(), dobro() e metade(). Faça também um programa que importe esse 
# módulo e use algumas dessas funções.

def aumentar(valor=0, taxa=0):
    resultado =  valor + (valor * taxa / 100)
    return resultado


def diminuir(valor=0, taxa=0):
    resultado = valor - (valor * taxa / 100)
    return resultado


def dobro(valor=0):
    resultado = valor * 2
    return resultado


def metade(valor=0):
    resultado = valor / 2
    return resultado


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.',',')
   