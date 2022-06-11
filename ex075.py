"""Exercício Python 075: Desenvolva um programa que leia quatro
valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""

numeros = (int(input('Número 1: ')), int(input('Número 2: ')), int(input('Número 3: ')), int(input('Número 4: ')))
print(f'Números digitados: \n{numeros}\n')
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O primeiro valor 3 está na posição {numeros.index(3)}')
else:
    print(f'O valor 3 apareceu 0 vezes')
print('Os números pares são: ', end='')
for num in numeros:
    if num % 2 == 0 and num != 0:
        print(num, end=', ')
