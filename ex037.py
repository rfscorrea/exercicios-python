"""Exercício Python 037: Escreva um programa em Python que leia
um número inteiro qualquer e peça para o usuário escolher qual
será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal."""

num = int(input('Número inteiro: '))
print('Opções:  [1] binário \n         [2] octal \n         [3] hexadecimal\n')
resp = int(input('Escolha: '))
if resp == 1:
    print('{} convertido para binário vale: {}'.format(num, bin(num)[2:]))
elif resp == 2:
    print('{} convertido para octal vale: {}'.format(num, oct(num)[2:]))
elif resp == 3:
    print('{} convertido para hexadecimal vale: {}'.format(num, hex(num)[2:]))
else:
    print('Resposta inválida!')
