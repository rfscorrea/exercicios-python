"""Exercício Python 086: Crie um programa que declare uma matriz
de dimensão 3x3 e preencha com valores lidos pelo teclado. No final,
mostre a matriz na tela, com a formatação correta."""

matriz = [[int(input('a11: ')), int(input('a12: ')), int(input('a13: '))],
          [int(input('a21: ')), int(input('a22: ')), int(input('a23: '))],
          [int(input('a31: ')), int(input('a32: ')), int(input('a33: '))]]
for lin in range(0, 3):
    for col in range(0, 3):
        print(f'({matriz[lin][col]:^10})', end=' ')
    print('')
