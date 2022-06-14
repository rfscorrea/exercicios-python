"""Exercício Python 092: Crie um programa que leia nome,
ano de nascimento e carteira de trabalho e cadastre-o (com idade)
em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário
receberá também o ano de contratação e o salário. Calcule e acrescente,
além da idade, com quantos anos a pessoa vai se aposentar."""

from operator import getitem
from datetime import datetime

nome = input('Nome: ')
ano = int(input('Ano de nascimento: '))
idade = datetime.now().year - ano
carteiraTrabalho = int(input('Carteira de trabalho: '))

dicio = {'nome': nome, 'idade': idade,
         'carteiraTrabalho': carteiraTrabalho}

if carteiraTrabalho != 0:
    anoContratacao = int(input('Ano de contratação: '))
    salario = float(input('Salário: R$'))
    anosContribuicao = datetime.now().year - anoContratacao
    idadeAposentar = 60
    idade = int(getitem(dicio, 'idade'))

    if anosContribuicao < 35:
        idadeAposentar = idade + (35 - anosContribuicao)
        if idadeAposentar < 60:
            idadeAposentar = 60

    dicio['anoContratacao'] = anoContratacao
    dicio['salario'] = salario
    dicio['aposentar'] = idadeAposentar
for k, v in dicio.items():
    print(f'{k}: {v}')
