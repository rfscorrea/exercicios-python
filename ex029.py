"""Exercício Python 029: Escreva um programa que leia a velocidade
de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo
que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite."""

v = int(input('Digite a velocidade do carro em Km/h: '))
if v > 80:
    multa = int((v - 80) * 7)
    print('Você ultrapassou o limite de velocidade e foi multado em R${}'.format(multa))

