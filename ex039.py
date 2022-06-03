"""Exercício Python 039: Faça um programa que leia o ano de nascimento
de um jovem e informe, de acordo com a sua idade, se ele ainda vai se
alistar ao serviço militar, se é a hora exata de se alistar ou se já
passou do tempo do alistamento. Seu programa também deverá mostrar o tempo
que falta ou que passou do prazo."""

ano = int(input('Ano de nascimento: '))
idade = 2022 - ano
if idade == 17 or idade == 18:
    print('É hora de se alistar!')
elif idade < 17:
    print('Ainda não é hora para se alistar! \nFaltam {} anos.'.format(18 - idade))
else:
    print('Você já deveria ter se alistado! \nO prazou foi excedido em {} anos'.format(idade - 18))

