"""Exercício Python 099: Faça um programa que tenha uma função
chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior."""

numeros = list()


def maior(* args):
    maior_valor = int()
    for valor in args:
        if valor > maior_valor:
            maior_valor = valor
    print(maior_valor)


maior(1, 5, 9, 8, 10, 54, 8)
maior(0, 1, 65, 321, 547, 21, 54, 0)
maior(1, 1, 1, 2, 5, 4, 6, 8, 10, 15, 321, 5456,)
