"""Exercício Python 008: Escreva um programa que leia um valor em
metros e o exiba convertido em centímetros e milímetros."""
metro = float(input('Insira um valor em metros: '))
cm = metro * 100
mm = metro * 1000
print('Valor em Metro: {} m \nCentímetro: {} cm \nMilímetro: {} mm'.format(metro, cm, mm))
