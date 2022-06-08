"""Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro
termo e a razão de uma PA, mostrando os 10 primeiros termos da
progressão usando a estrutura while.
"""

a1 = float(input('Primeiro termo: '))
r = float(input('Razão: '))
n = int(1)
print('=== PA ===')
while n != 10:
    print('{} → '.format(a1 + (n-1)*r), end='')
    n += 1
print('{}'.format(a1 + 9*r))

