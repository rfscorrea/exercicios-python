"""Exercício Python 051: Desenvolva um programa que leia o primeiro
termo e a razão de uma PA. No final, mostre os 10 primeiros termos
dessa progressão.
"""

a1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
print('Os dez primeiros termos de uma PA de primeiro termo {} e razão {} são: '.format(a1, r))
for c in range(0, 10):
    print(a1 + (c * r))
