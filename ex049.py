"""Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de
um número que o usuário escolher, só que agora utilizando um laço for.
"""

n = int(input('Número: '))
print('A tabuada de {} é: '.format(n))
for c in range(0, 11):
    print('{} x {} = {}'.format(n, c, n*c))
