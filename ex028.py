"""Exercício Python 028: Escreva um programa que faça o computador
'pensar' em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador. O programa deverá
escrever na tela se o usuário venceu ou perdeu."""

from random import randint
num = int(randint(0, 5))
a = int(input('Tente adivinhar qual o número de 0 a 5 escolhido pelo computador: '))
if a == num:
    print('O número escolhido foi {} \nVocê acertou!'.format(num))
else:
    print('O número escolhido foi {} \nVocê errou!'.format(num))
