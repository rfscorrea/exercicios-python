"""Exercício Python 077: Crie um programa que tenha uma tupla
com várias palavras (não usar acentos). Depois disso, você deve
mostrar, para cada palavra, quais são as suas vogais.
"""

variasPalavras = ('Costelas', 'Novidade', 'Pinguim', 'Alpinista', 'Adao',
                  'Armadura', 'Bulbo', 'Dobrado', 'Pose', 'Hermetico')
vogais = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
for c in range(0, len(variasPalavras)):
    umaPalavra = variasPalavras[c]
    print(f'\nA palavra {umaPalavra} tem as vogais: ', end='')
    for x in range(0, len(umaPalavra)):
        if umaPalavra[x] in vogais:
            print(f'{umaPalavra[x]}', end=' ')
