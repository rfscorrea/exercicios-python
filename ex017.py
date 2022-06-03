"""Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto
e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa."""

from math import sqrt

a = float(input('Cateto 1: '))
b = float(input('Cateto 2: '))
hip = sqrt(a*a + b*b)
print('Um triângulo retângulo com catetos a = {} e b = {}, tem hipotenusa de comprimento {}'.format(a, b, hip))
