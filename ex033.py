"""Exercício Python 033: Faça um programa que leia três números e
mostre qual é o maior e qual é o menor."""

maior = int(0)
print('/////////////// Digite três números inteiros: ///////////////')
a = int(input('1º número: '))
b = int(input('2º número: '))
c = int(input('3º número: '))
if a >= b >= c or a >= c >= b:
    maior = a
elif b >= a >= c or b >= c >= a:
    maior = b
else:
    maior = c
print('Você digitou os número {}, {}, {} \nO maior entre eles é o {}'.format(a, b, c, maior))
