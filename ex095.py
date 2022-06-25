"""Exercício Python 095: Aprimore o desafio 93 para que ele funcione
com vários jogadores, incluindo um sistema de visualização de detalhes
do aproveitamento de cada jogador."""

infoDoJogador = dict()
jogadoresCadastrados = dict()
resposta = str()
totalJogadoresCadastrados = int(0)
totalGols = int(0)


while True:     # cadastrar jogadores
    infoDoJogador.clear()
    resposta = str(input('Deseja cadastrar mais um jogador? [s]/[n]: '))
    if resposta == 's':

        infoDoJogador['nomeJogador'] = str(input('Nome do jogador: '))
        infoDoJogador['totalDePartidasJogadas'] = int(input('Total de partidas jogadas: '))

        totalPartidas = infoDoJogador['totalDePartidasJogadas']

        for c in range(0, totalPartidas):
            infoDoJogador[f'totalDeGolsPartida{c+1}'] = int(input(f'Total de gols na partida {c+1}: '))
            totalGols += infoDoJogador[f'totalDeGolsPartida{c+1}']

        infoDoJogador['totalDeGolsNoCampeonato'] = totalGols
        totalJogadoresCadastrados += 1
        jogadoresCadastrados['{}'.format(infoDoJogador['nomeJogador'])] = infoDoJogador

    elif resposta == 'n':
        break

while True:     # visualizar jogadores
    resposta = input('Deseja ver algum jogador? [s]/[n]: ')

    if resposta == 's':

        if len(jogadoresCadastrados) == 0:
            print('Nenhum jogador foi cadastrado')
            break
        else:
            print('========= Lista de jogadores =========')
            for k in jogadoresCadastrados.keys():
                print(f'[{k}]')
            print('======================================')

            resposta = input('Qual jogador deseja ver? ')
            for k, v in jogadoresCadastrados[f'{resposta}'].items():
                print(f'{k} = {v}')

    elif resposta == 'n':
        break
