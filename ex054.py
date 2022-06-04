"""Exercício Python 054: Crie um programa que leia o ano de
nascimento de sete pessoas. No final, mostre quantas pessoas
ainda não atingiram a maioridade e quantas já são maiores."""

maior = int(0)
menor = int(0)
ano = int(0)
for c in range(0, 7):
    ano = int(input('Ano de nascimento: '))
    if (2022 - ano) >= 18:
        maior += 1
    else:
        menor += 1
print('{} pessoas já atingiram a maioridade e {} ainda são menores'.format(maior, menor))
