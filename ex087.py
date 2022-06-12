"""Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha."""

"""matriz = [
    [int(input('a11: ')), int(input('a12: ')), int(input('a13: '))],
    [int(input('a21: ')), int(input('a22: ')), int(input('a23: '))],
    [int(input('a31: ')), int(input('a32: ')), int(input('a33: '))]
]"""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for lin in range(0, 3):
    for col in range(0, 3):
        matriz[lin][col] = int(input(f'a{lin+1}{col+1}: '))

somaPar = 0
for lin in range(0, 3):
    for col in range(0, 3):
        if matriz[lin][col] % 2 == 0 and matriz[lin][col] != 0:
            somaPar += matriz[lin][col]

somaTerceiraColuna = 0
for lin in range(0, 3):
    somaTerceiraColuna += matriz[lin][2]

maiorSegundaLinha = 0
for col in range(0, 3):
    if matriz[1][col] > maiorSegundaLinha:
        maiorSegundaLinha = matriz[1][col]
print(f'Soma dos valores pares digitado: {somaPar}'
      f'\nA soma dos valores da terceira coluna: {somaTerceiraColuna}'
      f'\nO maior valor da segunda linha: {maiorSegundaLinha}')
