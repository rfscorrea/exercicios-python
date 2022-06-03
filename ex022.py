"""Exercício Python 022: Crie um programa que leia o nome completo de
uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo sem considerar espaço.
- Quantas letras tem o primeiro nome."""


nome = str(input('Digite seu nome completo: '))
juntar = str('-'.join(nome))
nome.strip()
print('Maiúsculas: {} \nMinúsculas: {}'.format(nome.upper(), nome.lower()))
nome1 = nome.split()
letrasPrimeiro = int(len(nome1[0]))
letrasTotal = int(len(''.join(nome1)))
print('No total são {} letras \nO primeiro nome tem {} letras'.format(letrasTotal, letrasPrimeiro))
