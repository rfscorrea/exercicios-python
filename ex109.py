"""Exercício Python 109: Modifique as funções que form criadas no desafio 107
para que elas aceitem um parâmetro a mais, informando se o valor retornado por
elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108."""

from modulos import moeda

valor = float(input('Valor: '))
aumento = int(input('Aumento: '))
desconto = int(input('Desconto: '))

print(f'Valor: {moeda.moeda(valor)}')
print(f'Aumento de {aumento}%: {moeda.aumentar(aumento, valor)}')
print(f'Desconto de {desconto}%: {moeda.diminuir(desconto, valor)}')
print(f'Metade: {moeda.metade(valor)}')
