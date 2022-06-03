"""Exercício Python 023: Faça um programa que leia um número de 0 a 9999
e mostre na tela cada um dos dígitos separados."""

# solução 1
n = str(input('Digite um número entre 0 e 9999: '))
print('{} {} {} {}'.format(n[0:1], n[1:2], n[2:3], n[3:]))

# solução 2:
n = int(input('Digite um número entre 0 e 9999: '))
u = n % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(m, c, d, u)
