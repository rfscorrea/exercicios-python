"""Exercício Python 100: Faça um programa que tenha uma lista chamada
números e duas funções chamadas sorteia() e somaPar(). A primeira função
vai sortear 5 números e vai colocá-los dentro da lista e a segunda função
vai mostrar a soma entre todos os valores pares sorteados pela função anterior."""

from random import randint


def sorteia():
    for c in range(0, 5):
        num = randint(0, 100)
        numeros.append(num)
    print(f'Numeros sorteados: {numeros}')


def somapar():
    soma = int()
    numeros_pares = list()
    for i, v in enumerate(numeros):
        if v % 2 == 0:
            numeros_pares.append(v)
            soma += v
    print(f'Números pares: {numeros_pares}\n'
          f'Soma entre eles: {soma}')


numeros = list()
sorteia()
somapar()
