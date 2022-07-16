"""Exercício Python 107: Crie um módulo chamado moeda.py
que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções."""

from modulos import moeda

valor = float(input('Digite um valor: R$'))
aumento = int(input('Porcentagem do aumento: '))
desconto = int(input('Porcentagem do desconto: '))
valor_maior = moeda.aumentar(aumento, valor)
valor_menor = moeda.diminuir(desconto, valor)
valor_dobro = moeda.dobro(valor)
valor_metade = moeda.metade(valor)

print(f'Valor digitado: {valor}'
      f'\n{aumento}% de aumento fica: {valor_maior}'
      f'\n{desconto}% de desconto: {valor_menor}'
      f'\ndobro: {valor_dobro}'
      f'\nmetade: {valor_metade}')
