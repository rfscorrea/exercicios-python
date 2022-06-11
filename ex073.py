"""Exercício Python 073: Crie uma tupla preenchida com os 20
primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time do Flamengo."""

tabela = ('Palmeiras', 'Corinthians', 'Athletico-PR', 'Atlético-MG',
          'Coritiba', 'São Paulo', 'Internacional', 'Fluminense',
          'América-MG', 'Santos', 'Bragantino', 'Ceará', 'Goiás', 'Flamengo',
          'Botafogo', 'Avaí', 'Cuiabá', 'Atlético-GO', 'Juventude', 'Fortaleza')

print(f'5 primeiros colocados: \n{tabela[0:5]}')
print(f'4 último colocados: \n{tabela[-1:-5:-1]}')
print(f'Em ordem alfabética: \n{sorted(tabela)}')
print(f'O Flamengo está na {tabela.index("Flamengo")+1}º posição')
