# Faça um mini-sistema que utilize o interactive Help do Python. O usuário vai 
# digitar o comando e o manual vai aparecer. Quando o usuário digitar palavra
# FIM', o programa se encerrará.

#Obs: Usar cores
from datetime import sleep

cores = ('\033[m',        # 0 - sem cor
         '\033[30;41m',   # 1 - vermelho
         '\033[30;42m'    # 2 - verde
         '\033[30;43m'    # 3 - amarelo
         '\033[30;44m'    # 4 - azul
         '\033[30;45m'    # 5 - roxo
         '\033[7;30m'     # 6 - branco
         )
