"""Exercício Python 072: Crie um programa que tenha uma
tupla totalmente preenchida com uma contagem por extenso,
de zero até vinte. Seu programa deverá ler um número pelo
teclado (entre 0 e 20) e mostrá-lo por extenso."""

numExtenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
              'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',
              'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

num = int(input('número de 0 a 20: '))
print(f'O número {num} escrito por extenso é: {numExtenso[num]}')