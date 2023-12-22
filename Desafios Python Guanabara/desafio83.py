from time import sleep

#Crie um programa onde o usuário digite uma expressao
#qualquer que use parenteses. O programa deverá
#analisar se a expressao passada está com os parenteses
#abertos e fechados, na ordem correta

def verificar_parenteses(expressao):
    pilha = []

    for caractere in expressao:
        if caractere == '(':
            pilha.append('(')
        elif caractere == ')':
            if len(pilha) > 0 and pilha[-1] == '(':
                pilha.pop()
            else:
                pilha.append(')')
                break
    if len(pilha) == 0:
        return True
    else:
        return False

expressao = input('Digite uma expressão matemática: ')
if verificar_parenteses(expressao):
    print('Expressão válida! Os parenteses estão nas posições corretas. Parabéns!!')
else:
    print('EXpressão inválida! Verifique as posições dos parenteses e tente novamente!! Obrigado.')