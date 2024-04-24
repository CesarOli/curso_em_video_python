#Faça um programa que tenha uma função chamada escreva() que receba um texto
# qualquer como parametro e mostre uma mensagem com tamanho adaptável.


def l(comprimento):
    print('-' * comprimento)


def escreva(texto):
    comprimento_texto = len(texto)
    l(comprimento_texto)
    print(texto)
    l(comprimento_texto)


texto = input("Digite um texto qualquer: ")
escreva(texto)
