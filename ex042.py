"""Exercício Python 042: Refaça o DESAFIO 035 dos triângulos,
acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes"""

a = float(input('1º lado: '))
b = float(input('2º lado: '))
c = float(input('3º lado: '))
if abs(b-c) < a < (b + c) and abs(a-c) < b < (a + c) and abs(b-a) < c < (b + a):
    if a == b == c:
        print('O triângulo de lados {}, {} e {} é: Equilátero'.format(a, b, c))
    elif a != b != c:
        print('O triângulo de lados {}, {} e {} é: Escaleno'.format(a, b, c))
    else:
        print('O triângulo de lados {}, {} e {} é: Isósceles'.format(a, b, c))
else:
    print('Pela condição de existência de triângulos, eles lados não podem formar um triângulo!')
