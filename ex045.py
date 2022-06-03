"""Exercício Python 045: Crie um programa que faça o computador
jogar Jokenpô com você"""

from random import choice
eu = str(input('Pedra, papel ou tesoura?: ')).strip().lower()
computador = choice(['pedra', 'papel', 'tesoura'])
if eu == 'papel':
    if computador == 'pedra':
        print('\033[32mGanhou\033[m \nVocê escolheu \033[35m{}\033[m e o computador escolheu \033[36m{}\033[m'.format(eu, computador))
    elif computador == 'tesoura':
        print('\033[31mPerdeu\033[m \nVocê escolheu \033[35m{}\033[m e o computador escolheu \033[36m{}\033[m'.format(eu, computador))
    else:
        print('\033[37mEmpate\033[m \nVocê escolheu \033[35m{}\033[m e o computador escolheu \033[36m{}\033[m'.format(eu, computador))

elif eu == 'pedra':
    if computador == 'tesoura':
        print('\033[32mGanhou\033[m \nVocê escolheu \033[35m{}\033[m e o computador escolheu \033[36m{}\033[m'.format(eu, computador))
    elif computador == 'papel':
        print('\033[31mPerdeu\033[m \nVocê escolheu \033[35m{}\033[m e o computador escolheu \033[36m{}\033[m'.format(eu, computador))
    else:
        print('\033[37mEmpate\033[m \nVocê escolheu \033[35m{}\033[m e o computador escolheu \033[36m{}\033[m'.format(eu, computador))

elif eu == 'tesoura':
    if computador == 'papel':
        print('\033[32mGanhou\033[m \nVocê escolheu \033[35m{}\033[m e o computador escolheu \033[36m{}\033[m'.format(eu, computador))
    elif computador == 'pedra':
        print('\033[31mPerdeu\033[m \nVocê escolheu \033[35m{}\033[m e o computador escolheu \033[36m{}\033[m'.format(eu, computador))
    else:
        print('\033[37mEmpate\033[m \nVocê escolheu \033[35m{}\033[m e o computador escolheu \033[36m{}\033[m'.format(eu, computador))

else:
    print('\033[31mEscolha inválida!\033[m')
