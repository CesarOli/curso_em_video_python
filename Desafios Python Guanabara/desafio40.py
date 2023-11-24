print('\033[1;31mO "Clááássico" da Média.\033[m\n')

nota1 = float(input('Digite aqui caro aluno, a nota da sua primeira avaliação: '))
nota2 = float(input('Digite aqui caro aluno, a nota da sua segunda avaliação: '))
media = (nota1 + nota2) / 2
print('\nSua média foi de {}.'.format(media))
if media < 5:
    print('Você foi \033[1;31mREPROVADO\033[m, estude mais para as próximas avaliações.')
elif 5 <= media <= 6.9:
    print('Voce está em \033[1;33mRECUPERAÇÃO\033[m, ainda da tempo de passar de ano. Seja sábio!')
else:
    print('APROVADO, PARABÉÉÉNS!!!')
