"""Exercício Python 103: Faça um programa que tenha uma função chamada
ficha(), que receba dois parâmetros opcionais: o nome de um jogador e
quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do
jogador, mesmo que algum dado não tenha sido informado corretamente."""


def ficha(nome='none', gols=0):
        print(f'Nome do jogador: {nome} \nTotal de gols: {gols} gols')


a = input('Nome jogador: ')
b = input('Gols feitos: ')

if b.isnumeric():
    b = int(b)
else:
    b = 0
if a.strip() == '':
    ficha(gols=b)
else:
    ficha(a, b)
