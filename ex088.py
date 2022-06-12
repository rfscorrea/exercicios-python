"""Exercício Python 088: Faça um programa que ajude um jogador
da MEGA SENA a criar palpites.O programa vai perguntar quantos
jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada
jogo, cadastrando tudo em uma lista composta."""

import random
nJogos = int(input('Quantos jogos serão gerados?: '))
lista = []
for c in range(0, nJogos):
    lista.append(random.sample(range(1, 60), k=6))
print(lista)
