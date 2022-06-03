"""Exercício Python 038: Escreva um programa que leia dois números
inteiros e compare-os. mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais"""

n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))
if n1 > n2:
    print('O primeiro valor é maior: {} > {}'.format(n1, n2))
elif n2 > n1:
    print('O segundo valor é maior: {} > {}'.format(n2, n1))
else:
    print('Não existe valor maior, os dois são iguais: {} = {}'.format(n1, n2))
