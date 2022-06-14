"""Exercício Python 091: Crie um programa onde 4 jogadores joguem
um dado e tenham resultados aleatórios. Guarde esses resultados em
um dicionário em Python. No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado."""

from random import randint
from operator import itemgetter

dicio = dict()
for c in range(1, 5):
    dado = randint(1, 6)
    dicio[f'jogador{c}'] = dado

ranking = sorted(dicio.items(), key=itemgetter(1), reverse=True)
print(ranking)

for i, v in enumerate(ranking):
    print(f'{i+1}º colocado: {v[0]} que tirou {v[1]}')
