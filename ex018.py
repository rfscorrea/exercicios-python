""" Exercício Python 018: Faça um programa que leia um ângulo
qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo. """

from math import sin, cos, tan, radians

ang = float(input('Digite um ângulo em graus: '))
angr = radians(ang)
print('O ângulo {}º tem valores de: \nSeno = {} \nCosseno = {} '
      '\nTangente = {}'.format(ang, sin(angr), cos(angr), tan(ang)))
