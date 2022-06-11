"""Exercício Python 074: Crie um programa que vai gerar
cinco números aleatórios e colocar em uma tupla. Depois
disso, mostre a listagem de números gerados e também indique
o menor e o maior valor que estão na tupla."""

from random import randint
numeros = (randint(1, 1000), randint(1, 1000), randint(1, 1000), randint(1, 1000), randint(1, 1000),)
numMaior = 0
numMenor = 1001
for num in numeros:
    if num > numMaior:
        numMaior = num
    elif num < numMenor:
        numMenor = num
print(f'Foram gerados os números: \n{numeros}')
print(f'\nO maior entre eles é: {numMaior}')
print(f'O menor entre eles é: {numMenor}')
