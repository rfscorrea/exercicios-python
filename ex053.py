"""Exercício Python 053: Crie um programa que leia uma frase
qualquer e diga se ela é um palíndromo, desconsiderando os espaços."""

frase = str(input('Frase: ')).strip().capitalize().split()
fraseJunta = ' '.join(frase)
inverso = ''
for c in range(len(frase)-1, -1, -1):
    inverso += frase[c]
print(inverso)
if fraseJunta == inverso:
    print('A frase: "{}" é um palíndromo'.format(fraseJunta))
else:
    print('A frase: "{}" não é um palíndromo'.format(fraseJunta))
