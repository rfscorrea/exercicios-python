"""Exercício Python 104: Crie um programa que tenha a função
leiaInt(), que vai funcionar de forma semelhante 'a função input()
do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ')"""


def leiaint(msg=''):
    global teste
    n = input(msg)
    if n.isnumeric():
        print(f'Valor digitado: {int(n)}')
    else:
        teste = -1


teste = 0
while True:
    leiaint('Digite um numero: ')
    if teste == -1:
        print('ERRO')
        break
