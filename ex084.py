"""Exercício Python 084: Faça um programa que leia nome e peso
de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves."""

matriz = []
pessoasTotal = 1
pessoasLeves = []
pessoasPesadas = []
cliente = [input('Nome: '), int(input('Peso: '))]
matriz.append(cliente[:])

while True:
    resposta = input('Deseja cadastrar mais uma pessoa? [s]/[n]')
    if resposta == 's':
        pessoasTotal += 1
        cliente = [input('Nome: '), int(input('Peso: '))]
        matriz.append(cliente[:])
    elif resposta == 'n':
        break

for pessoa in matriz:
    if pessoa[1] >= 100:
        pessoasPesadas.append(pessoa[0])
    else:
        pessoasLeves.append(pessoa[0])

print(f'Foram cadastradas {pessoasTotal} pessoas '
      f'\nAs pessoas com mais de 100kg são: {pessoasPesadas}'
      f'\nAs pessoas com menos de 100Kg são: {pessoasLeves}')
