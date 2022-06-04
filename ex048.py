"""Exercício Python 048: Faça um programa que calcule a soma
entre todos os números ímpares que são múltiplos de três e que se encontram
no intervalo de 1 até 500."""

soma = int(0)
print('No intervalo [1, 500], são múltiplos de 3: ')
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        print(c, end=' ')
print('\nA soma desses números vale: {}'.format(soma))
