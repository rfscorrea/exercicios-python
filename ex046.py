"""ExercΓ­cio Python 046: FaΓ§a um programa que mostre na tela uma
contagem regressiva para o estouro de fogos de artifΓ­cio, indo de 10 atΓ© 0,
com uma pausa de 1 segundo entre eles.
"""

from time import sleep
print('{} CONTAGEM REGRESSIVA {}'.format('//'*8, '//'*8))
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('ππππππππππππππππππππππ')
