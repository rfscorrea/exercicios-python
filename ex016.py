"""Exercício Python 016: Crie um programa que leia um número Real qualquer pelo
teclado e mostre na tela a sua porção Inteira."""

from math import trunc
n = float(input('Digite um número real qualquer: '))
nt = trunc(n)
print('Você digitou o número {} \nSua porção inteira é {}'.format(n, nt))
