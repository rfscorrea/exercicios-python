"""Exercício Python 102: Crie um programa que tenha
uma função fatorial() que receba dois parâmetros: o
primeiro que indique o número a calcular e outro chamado
show, que será um valor lógico (opcional) indicando se será
mostrado ou não na tela o processo de cálculo do fatorial."""

from time import sleep


def fatorial(n, show=True):
    i = 1
    fat = n
    while i < n:
        fat *= n - i
        i += 1
    if show is True:
        print(f'{n} x ', end='')
        for i in range(n-1, 1, -1):
            sleep(1)
            print(f'{i} x ', end='')
        sleep(1)
        print('1 = ', end='')
        sleep(1)
        print(f'{fat}')
    else:
        return fat



print(fatorial(5, show=False))
