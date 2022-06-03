"""Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa
tem na carteira e mostre quantos dólares ela pode comprar."""

#Utilizando a cotação do dia 29/05/2022 1 Real = 0,21 Dólar
dinheiro = float(input('Digite quanto dinheiro você tem: '))
dolar = dinheiro * 0.21
print('Você tem {:.2f} Reais e pode comprar {:.2f} dólars'.format(dinheiro, dolar))
