"""Exercício Python 055: Faça um programa que leia o peso de
cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos."""

maior = float(0)
menor = float(1000)
peso = float()
for c in range(0, 5):
    peso = float(input('Peso da {}º pessoa: '.format(c+1)))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('Maior peso: {} \nMenor peso: {}'.format(maior, menor))
