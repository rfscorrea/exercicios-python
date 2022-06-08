"""Exercício Python 059: Crie um programa que leia dois valores e
mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso."""

i = int()  # opções de resposta para o menu
print('Digite dois números quaisquer: \n')
valor1 = int(input('Primeiro número: '))
valor2 = int(input('Segundo número: '))
soma = valor1 + valor2
multiplicacao = valor1 * valor2
while i != 5:
    print('=== O que deseja fazer? ===')
    print(' [1] somar\n '
          '[2] multiplicar\n '
          '[3] maior\n '
          '[4] novos números\n'
          ' [5] sair do programa')
    print('===========================')
    i = int(input('Opção: '))
    if i == 1:
        print('SOMA: {} + {} = {}'.format(valor1, valor2, soma))
    elif i == 2:
        print('MULTIPLICAÇÃO: {} x {} = {}'.format(valor1, valor2, multiplicacao))
    elif i == 3:
        print('MAIOR: {} > {}'.format(max(valor1, valor2), min(valor1, valor2)))
    elif i == 4:
        valor1 = int(input('Primeiro número: '))
        valor2 = int(input('Segundo número: '))
        soma = valor1 + valor2
        multiplicacao = valor1 * valor2
