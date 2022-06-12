"""Exercício Python 078: Faça um programa que leia 5 valores
numéricos e guarde-os em uma lista. No final, mostre qual foi
o maior e o menor valor digitado e as suas respectivas posições
na lista. """

lista = [0, 0, 0, 0, 0]
maior = 0
posicaoMaior = 0
lista[0] = int(input('Número 1: '))
menor = lista[0]
posicaoMenor = 0
for c in range(1, 5):
    lista[c] = int(input(f'Número {c}: '))
for pos, num in enumerate(lista):
    if num > maior:
        maior = num
        posicaoMaior = pos
    elif num < menor:
        menor = num
        posicaoMenor = pos
print(f'Números digitados {lista}')
print(f'Maior número {maior} na posição {posicaoMaior}')
print(f'Menor número {menor} na posição {posicaoMenor}')
