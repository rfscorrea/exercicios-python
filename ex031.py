"""Exercício Python 031: Desenvolva um programa que pergunte a distância
de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km
para viagens de até 200Km e R$0,45 parta viagens mais longas."""

d = float(input('Digite a distância em km: '))
p = float(0)
if d <= 200:
    p = d * 0.5
else:
    p = d * 0.45
print('Você viajou {}km \nO valor cobrado será R${:.2f}'.format(d, p))
