"""Exercício Python 065: Crie um programa que leia vários
números inteiros pelo teclado. No final da execução, mostre
a média entre todos os valores e qual foi o maior e o menor
valores lidos. O programa deve perguntar ao usuário se ele
quer ou não continuar a digitar valores."""

maior = int()
numero = int()
soma = int()
i = int()
resposta = str('a')
condicao = int()

while condicao != 1:
    numero = int(input('Número: '))
    soma += numero
    i += 1
    maior = numero

    while True:
        resposta = str(input('Deseja digitar mais valores? [S] // [N]: ')).strip().lower()
        if resposta != 's' and resposta != 'n':
            print('INVÁLIDO')
        elif resposta == 's':
            numero = int(input('Número: '))
            soma += numero
            i += 1
            if numero > maior:
                maior = numero
        elif resposta == 'n':
            condicao = 1
            break

print('Média entre os valores digitados: {} \nO maior valor digitado '
      'foi: {}'.format(soma/i, maior))
