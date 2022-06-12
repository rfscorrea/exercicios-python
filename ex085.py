"""Exercício Python 085: Crie um programa onde o usuário
possa digitar sete valores numéricos e cadastre-os em uma
lista única que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente."""

valores = [[], []]

for c in range(0, 7):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0 and valor != 0:
        valores[0].append(valor)
    elif valor % 2 != 0 and valor != 0:
        valores[1].append(valor)

valores[0].sort()
valores[1].sort()

print(f'Valores pares: {valores[0]}'
      f'\nValores ímpares: {valores[1]}')
