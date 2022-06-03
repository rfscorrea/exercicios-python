"""Exercício Python 026: Faça um programa que leia uma frase
pelo teclado e mostre quantas vezes aparece a letra "A", em que
posição ela aparece a primeira vez e em que posição ela aparece a última vez."""

frase = str(input('Frase: '))
fraseFormatada = frase.strip().lower()
frasePrint = frase.strip().capitalize()
numeroDeA = fraseFormatada.count('a')
primeiroA = fraseFormatada.find('a')
ultimoA = fraseFormatada.rfind('a')

print('Frase: {} \n Há {} letras "a" nessa frase \nA primeira letra "a" aparece '
      'na posição {} \nA última letra "a" aparece na posição {}'.format(frasePrint, numeroDeA, primeiroA, ultimoA))
