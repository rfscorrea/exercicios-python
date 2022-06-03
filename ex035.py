"""Exercício Python 035: Desenvolva um programa que leia o
comprimento de três retas e diga ao usuário se elas podem ou
não formar um triângulo."""

print('//////////// Digite o comprimento de três reta: ////////////')
a = float(input('1º reta: '))
b = float(input('2º reta: '))
c = float(input('3º reta: '))
if abs(b-c) < a < (b + c) and abs(a-c) < b < (a + c) and abs(b-a) < c < (b + a):
    print('Essas retas, pela condição de existência de triângulos, podem formar um triângulo')
else:
    print('Essas retas, pela condição de existência de triângulos, não podem formar um triângulo')
