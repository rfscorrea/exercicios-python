"""Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em
metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que
cada litro de tinta pinta uma área de 2 metros quadrados."""

lar = float(input('Largura da parede em metros: '))
alt = float(input('Altura da parede em metros: '))
area = lar * alt
tinta = area / 2
print('Parede com: \nLargura {:.2f}m \nAltura {:.2f}m \nÁrea {:.2f}m²'.format(lar, alt, area))
print('Para pintá-la, serão necessários {:.2f} litros de tinta'.format(tinta))
