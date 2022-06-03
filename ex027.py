"""Exercício Python 027: Faça um programa que leia o nome
completo de uma pessoa, mostrando em seguida o primeiro e o
último nome separadamente."""

nome = str(input('Nome: '))
nomeFormatado = nome.strip().upper()
nomeSplitado = nome.strip().title().split()
n = len(nomeSplitado) - 1
print('Nome: {} \nPrimeiro nome: {} \nÚltimo nome: {}'.format(nomeFormatado, nomeSplitado[0], nomeSplitado[n]))
