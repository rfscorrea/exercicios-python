"""Exercício Python 050: Desenvolva um programa que leia seis
números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o."""

soma = int(0)
num = int(0)
cont = int(0)
for c in range(0, 6):
    num = int(input('{}º número: '.format(c+1)))
    if (num % 2) == 0 and num != 0:
        soma += num
        cont += 1
print('São {} números pares e a soma entre eles vale: {}'.format(cont, soma))
