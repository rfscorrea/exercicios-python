"""Exercício Python 012: Faça um algoritmo que leia o preço de um produto
e mostre seu novo preço, com 5% de desconto."""

preco = (float(input('Preço do produto: ')))
desconto = preco * 0.95
print('O preço digitado foi: R${:.2f} \nO preço atual, com 5% de desconto, é R${:.2f}'.format(preco, desconto))
