"""Exercício Python 114: Crie um código em Python que teste
se o site pudim está acessível pelo computador usado."""

import urllib.request

try:
    teste = urllib.request.urlopen('http://pudim.com.br/')
except Exception as e:
    print('Nao foi possivel conectar')
    print(f'Erro: {e.__class__}')
else:
    print('Site no ar')
