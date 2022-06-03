"""Exercício Python 025: Crie um programa que leia o nome de uma
pessoa e diga se ela tem "SILVA" no nome."""

nome = str(input('Nome: '))
nomeFormatado = nome.strip().upper()
nomeSplitado = nomeFormatado.split()
teste = 'SILVA' in nomeSplitado
print('Nome digitado: {} \nEsse nome possui "SILVA"?: {}'.format(nomeFormatado, teste))
