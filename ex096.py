"""Exercício Python 096: Faça um programa que tenha uma
função chamada área(), que receba as dimensões de um terreno
 (largura e comprimento) e mostre a área do terreno."""


def area(larg, comp):
    resultado = float(larg * comp)
    print(f'Terreno de dimensoes {larg}m x {comp}m possui area de {resultado:.2f} m2')


largura = float(input('Largura: '))
comprimento = float(input('Comprimento: '))
area(largura, comprimento)
