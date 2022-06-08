"""Exercício Python 060: Faça um programa que leia um número qualquer e
mostre o seu fatorial.

Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120"""

num = int(input('Digite um número: '))
fatorial = int(1)
for i in range(2, num+1):
    fatorial = fatorial * i
print('Fatorial de {}: {}! = {}'.format(num, num, fatorial))





