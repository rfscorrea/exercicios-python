"""Exercício Python 007: Desenvolva um programa que leia as
duas notas de um aluno, calcule e mostre a sua média."""

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('Nota 1: {} \nNota 2: {} \nMédia : {}'.format(n1, n2, media))
