"""Exercício Python 106: Faça um mini-sistema que utilize o
Interactive Help do Python. O usuário vai digitar o comando e
o manual vai aparecer. Quando o usuário digitar a palavra 'FIM',
o programa se encerrará."""

while True:
    comando = input('função ou biblioteca: ').strip().lower()
    if comando == 'fim':
        break
    else:
        help(comando)
