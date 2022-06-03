"""Exercício Python 014: Escreva um programa que converta uma temperatura digitando em
graus Celsius e converta para graus Fahrenheit."""

c = float(input('Digite a temperatura em celsius: '))
f = c * 1.8 + 32
print('{}º Celsius equivalem a {}º Fahrenheit'.format(c, f))
