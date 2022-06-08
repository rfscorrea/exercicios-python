"""Exercício Python 064: Crie um programa que leia vários números
inteiros pelo teclado. O programa só vai parar quando o usuário
digitar o valor 999, que é a condição de parada. No final, mostre
quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag)."""

numeros = {}
i = int()
soma = int()
num = int()
while num != 999:
    num = int(input('Número: '))
    numeros[i] = num
    soma += numeros[i]
    i += 1
print('Você digitou {} números\nA soma entre eles vale {}'.format(i-1, soma-999))
