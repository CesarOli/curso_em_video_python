# Faça um programa que tenha uma função notas() que pode receber várias notas de
# alunos e vai retornar um dicionário com as seguintes informações: 
# - Quantidade de notas 
# - A maior nota
# - A menor nota 
# - A média da turma - 
# - A situação (opcional)
# - Adicionar tbm o docstring da função.

# Primeira Solução
from time import sleep

def notas(*nota, situacao=False):

    """
        Calcula estatísticas de uma lista de notas e por opção do usuário retorna a situação do aluno.

        Parâmetros:
            *nota (float): Uma sequência de notas dos alunos.
            situacao (bool, opcional): Indica se a situação do aluno deve ser incluída no resultado.
                                        Se True, a função retorna a situação do aluno com base na média das notas.
                                        Se False (padrão), a função não inclui a situação do aluno no resultado.

        Retorna:
            dict: Um dicionário contendo as estatísticas das notas.
                As chaves são:
                    - 'total': O número total de notas fornecidas.
                    - 'maior': A maior nota dentre as fornecidas.
                    - 'menor': A menor nota dentre as fornecidas.
                    - 'média': A média das notas fornecidas.
                    - 'situacao' (opcional): A situação do aluno com base na média das notas, se situacao=True.
                                                Se situacao=False, essa chave não estará presente no dicionário.

        Exemplo:
            resultado = notas(10, 10, 8, situacao=True)
            print(resultado)
        """
    total_notas = len(nota)
    maior_nota = max(nota)
    menor_nota = min(nota)
    media = sum(nota) / len(nota)

    resultado = {'total': total_notas, 'maior': maior_nota, 'menor': menor_nota, 'média': media}

    if situacao:
        if media >= 5 and media <= 7:
            situacao = 'Sempre pode melhorar! Continue estudando.'
        elif media < 5:
            situacao = 'Estuda mano, tá ruim pra você.'
        else:
            situacao = 'É isso, continue assim!'
        
        resultado['situacao'] = situacao

    return resultado

# Programa Principal
sleep(1)
print('Primeira Solução')
resultado = notas(10, 0, 1.5, situacao=True)
sleep(1)
print(resultado)
sleep(0.5)


# Segunda Solução Corrigida e com a Docstring
'''from time import sleep

def notas(*nota, situacao=False):

    """
    Calcula estatísticas de uma lista de notas e por opção do usuário retorna a situação do aluno.

    Parâmetros:
        *nota (float): Uma sequência de notas dos alunos.
        situacao (bool, opcional): Indica se a situação do aluno deve ser incluída no resultado.
                                    Se True, a função retorna a situação do aluno com base na média das notas.
                                    Se False (padrão), a função não inclui a situação do aluno no resultado.

    Retorna:
        dict: Um dicionário contendo as estatísticas das notas.
              As chaves são:
                  - 'total': O número total de notas fornecidas.
                  - 'maior': A maior nota dentre as fornecidas.
                  - 'menor': A menor nota dentre as fornecidas.
                  - 'média': A média das notas fornecidas.
                  - 'situacao' (opcional): A situação do aluno com base na média das notas, se situacao=True.
                                            Se situacao=False, essa chave não estará presente no dicionário.

    Exemplo:
        resultado = notas(10, 10, 8, situacao=True)
        print(resultado)
    """
    total_notas = len(nota)
    maior_nota = max(nota)
    menor_nota = min(nota)
    media = sum(nota) / len(nota)

    if situacao:
        if media >= 5 and media <= 7:
            situacao = 'Sempre pode melhorar! Continue estudando.'
        elif media < 5:
            situacao = 'Estuda mano, tá ruim pra você.'
        else:
            situacao = 'É isso, continue assim!'
    
    else:
        situacao = None
    
    resultado = {'total': total_notas, 'maior': maior_nota, 'menor': menor_nota, 'média': media}

    if situacao:
        resultado['situacao'] = situacao

    return resultado

# Programa Principal
sleep(1.2)
print('Segunda Solução')
resultado = notas(0, 0, 8, situacao=True)
sleep(1)
print(resultado)
sleep(2)
print('Fim do Programa!')
sleep(0.5)
'''


# Terceira Solução, crição simples do dicionário

'''def notas(*notas, situacao = False):

    """
    Calcula estatísticas de uma lista de notas e por opção do usuário retorna a situação do aluno.

    Parâmetros:
        *nota (float): Uma sequência de notas dos alunos.
        situacao (bool, opcional): Indica se a situação do aluno deve ser incluída no resultado.
                                    Se True, a função retorna a situação do aluno com base na média das notas.
                                    Se False (padrão), a função não inclui a situação do aluno no resultado.

    Retorna:
        dict: Um dicionário contendo as estatísticas das notas.
              As chaves são:
                  - 'total': O número total de notas fornecidas.
                  - 'maior': A maior nota dentre as fornecidas.
                  - 'menor': A menor nota dentre as fornecidas.
                  - 'média': A média das notas fornecidas.
                  - 'situacao' (opcional): A situação do aluno com base na média das notas, se situacao=True.
                                            Se situacao=False, essa chave não estará presente no dicionário.

    Exemplo:
        resultado = notas(10, 10, 8, situacao=True)
        print(resultado)
    """
    r = dict()
    r['total'] = len(notas)
    r['maior'] = max(notas)
    r['menor'] = min(notas)
    r['média'] = sum(notas)/ len(notas)
    
    if situacao:
        if r['média'] >= 8:
            r['situação'] = 'Ta bem, continue assim!'
        elif r['média'] >= 5:
            r['situação'] = 'Tá bom, mas sempre dá pra melhorar, estude mais um pouco.'
        else:
            r['situação'] = 'Estude mais, ta precisando e será bom pra vc!'
        return r
    
# Programa Principal
resposta = notas(7.5, 7.5, 10, situacao=True)
print(resposta)
help(notas)'''
