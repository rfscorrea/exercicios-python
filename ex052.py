"""Exercício Python 052: Faça um programa que leia um número inteiro
e diga se ele é ou não um número primo.
"""
n = int(input('Número: '))
if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 and n == 1 and n != 2:
    print(n, 'não é primo')
else:
    print(n, 'é primo')
