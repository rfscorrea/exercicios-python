"""Exercício Python 068: Faça um programa que jogue par ou ímpar
com o computador. O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo."""

from random import randint

vitorias = 0
while True:
    jogador = input('Par ou ímpar? [P][I]: ').lower().strip()
    numComputador = randint(0, 10)
    numJogador = int(input('Sua jogada: '))
    soma = numComputador + numJogador
    if jogador == 'p':
        if soma % 2 == 0:
            print(f'Ganhou!! \nO computador escolheu {numComputador} \n{numJogador}+{numComputador} = {soma} é PAR')
            vitorias += 1
        else:
            print(f'Ganhou!! \nO computador escolheu {numComputador} \n{numJogador}+{numComputador} = {soma} é ÍMPAR')
            break
    if jogador == 'i':
        print(f'Ganhou!! \nO computador escolheu {numComputador} \n{numJogador}+{numComputador} = {soma} é ÍMPAR')
        if soma % 2 != 0:
            vitorias += 1
        else:
            print(f'Perdeu!! \nO computador escolheu {numComputador} \n{numJogador}+{numComputador} = {soma} é PAR')
            break
print(f'No total foram {vitorias} vitórias')
