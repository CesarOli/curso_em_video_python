print('\033[1;31mÍndice de Massa Corporal.\n\033[m')
kilo = float(input('Digite aqui o seu peso em Kilogramas (Kg): '))
altura = float(input('Digite aqui a sua altura em metros (exemplo: 1.60): '))
imc = kilo / (altura * altura)
print('\nSeu IMC atual é {:.1f}'.format(imc))
if imc < 18.5:
    print('''\033[0;31mVocê está abaixo do peso ideal. Isso pode ser apenas uma característica pessoal, 
mas também pode ser um sinal de desnutrição ou de algum problema de saúde.Procure um médico. \033[m''')
elif 18.5 <= imc <= 25.00:
    print('''\033[0;32mParabéns, você está com o peso normal. 
Recomendamos que mantenha hábitos saudáveis em seu dia a dia. 
Especialistas sugerem ingerir de 4 a 5 porções diárias de frutas, verduras e legumes, 
além da prática de exercícios físicos - pelo menos 150 minutos semanais.\033[m''')
elif 25.00 < imc <= 30.00:
    print('''\033[0;33mAtenção! Alguns quilos a mais já são suficientes para que algumas 
pessoas desenvolvam doenças associadas, como diabetes e hipertensão. É importante rever seus hábitos.
Procure praticar atividades físicas.\033[m''')
elif 30 < imc <= 40:
    print('''\033[0;34mSinal de alerta! O excesso de peso é fator de risco para desenvolvimento de outros problemas de saúde. 
A boa notícia é que uma pequena perda de peso já traz benefícios à saúde. 
Procure um médico para definir o tratamento mais adequado para você\033[m''')
else:
    print('''\033[0;31mSinal vermelho! Ao atingir este nível de IMC, o risco de doenças associadas é muito alto. '
Busque ajuda de um profissional de saúde; não perca tempo.\033[m''')
print('\nFIM.')
