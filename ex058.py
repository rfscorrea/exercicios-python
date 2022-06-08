"""Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o
computador vai "pensar" em um número entre 0 e 10. Só que agora o
jogador vai tentar adivinhar até acertar, mostrando no final quantos
palpites foram necessários para vencer."""

from random import randint
numeroComputador = int(randint(0, 10))
tentativas = int(1)
numeroUsuario = int(input('Digite um número de 0 a 10: '))
while numeroUsuario != numeroComputador:
    print('=== ERROU!!! ===\n=== Tente denovo ===')
    numeroUsuario = int(input('Digite um número de 0 a 10: '))
    tentativas += 1
print('\nA resposta certa era {} \nVocê acertou com {} tentativas'.format(numeroComputador, tentativas))
