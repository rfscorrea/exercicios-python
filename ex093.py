"""Exercício Python 093: Crie um programa que gerencie o
aproveitamento de um jogador de futebol. O programa vai
ler o nome do jogador e quantas partidas ele jogou. Depois
vai ler a quantidade de gols feitos em cada partida. No final,
tudo isso será guardado em um dicionário, incluindo o total de
gols feitos durante o campeonato.
"""

nomeJogador = input('Nome jogador: ')
partidasJogadas = int(input('Partidas jogadas: '))
dicio = dict()
golsTotal = 0
for c in range(1, partidasJogadas+1):
    gol = int(input(f'Gols feitos na partida {c}: '))
    golsTotal += gol
    dicio[f'partida {c}'] = gol
dicio['totalidade'] = golsTotal
for k, v in dicio.items():
    print(f'Gols na {k}: {v} gols')
