"""Exercício Python 032: Faça um programa que leia um ano qualquer e
mostre se ele é bissexto."""

a = int(input('Ano: '))
if (a % 100) != 0 and (a % 4) == 0:
    print('{} é um ano bisexto'.format(a))
elif (a % 400) == 0:
    print('{} é um ano bisexto'.format(a))
else:
    print('{} não é um ano bisexto'.format(a))
