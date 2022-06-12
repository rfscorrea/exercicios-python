"""Exercício Python 081: Crie um programa que vai ler vários
números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""

lista = [int(input('Número: '))]
while True:
    resposta = input('Deseja digitar mais? [s]/[n]: ')
    if resposta == 's':
        num = int(input('Número: '))
        lista.append(num)
    elif resposta == 'n':
        break
listaDecrescente = lista[:]
listaDecrescente.sort(reverse=True)
print(f'Valores digitados: {lista}')
print(f'Valores em ordem decrescente: {listaDecrescente}')
if 5 in lista:
    print(f'O valor 5 foi digitado e sua primeira aparição foi na posição {lista.index(5)}')
else:
    print('O valor 5 não foi digitado')
