"""Exercício Python 097: Faça um programa que tenha uma função
chamada escreva(), que receba um texto qualquer como parâmetro e
mostre uma mensagem com tamanho adaptável."""


def escreva(msg):
    tamanho= len(msg) + 2
    linha = '~' * tamanho
    print(f'{linha}'
          f'\n {msg}'
          f'\n{linha}')


escreva('Tas')
