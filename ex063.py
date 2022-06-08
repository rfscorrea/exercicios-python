"""Exercício Python 063: Escreva um programa que leia um número N
inteiro qualquer e mostre na tela os N primeiros elementos de uma
Sequência de Fibonacci. """

n = int(input('Digite: '))
numeros = {}
numeros[0] = 0
numeros[1] = 1
for c in range(2, n+2):
    numeros[c] = numeros[c-2] + numeros[c-1]
    print(numeros[c], end='→ ')
