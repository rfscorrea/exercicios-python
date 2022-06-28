"""Exercício Python 101: Crie um programa que tenha uma função
chamada voto() que vai receber como parâmetro o ano de nascimento
de uma pessoa, retornando um valor literal indicando se uma pessoa
tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições."""

from time import localtime


def voto(ano):
    global anoatual, idade
    idade = anoatual - ano
    if idade < 16:
        return idade, 'NEGADO'
    elif idade >= 70 or idade == 16 or idade == 17:
        return idade, 'OPCIONAL'
    else:
        return idade, 'OBRIGATORIO'


anoatual = (localtime()[0])
anonascimento = int(input('Ano de nascimento: '))
idade = int()

print(f'Com {voto(anonascimento)[0]} anos seu voto e {voto(anonascimento)[1]}')
