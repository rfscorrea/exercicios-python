"""Exercício Python 070: Crie um programa que leia o nome e o preço de
vários produtos. O programa deverá perguntar se o usuário vai continuar
ou não. No final, mostre:

A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato."""


produtos1000 = 0
nomeProduto = input('Nome do produto: ')
precoProduto = float(input('Preço do produto: '))
produtoMaisBarato_preco = precoProduto
produtoMaisBarato_nome = nomeProduto
precoTotal = precoProduto
if precoProduto > 1000:
    produtos1000 += 1
while True:
    flag = input('Cadastrar mais produtos? [s]/[n]: ')
    if flag == 's':
        nomeProduto = input('Nome do produto: ')
        precoProduto = float(input('Preço do produto: '))
        precoTotal += precoProduto
        if precoProduto < produtoMaisBarato_preco:
            produtoMaisBarato_nome = nomeProduto
            produtoMaisBarato_preco = precoProduto
        elif precoProduto > 1000:
            produtos1000 += 1
    elif flag == 'n':
        break
print(f'\nTotal gasto: R${precoTotal} \nProdutos acima de R$1000: {produtos1000} '
      f'\nProduto mais barato: {produtoMaisBarato_nome} por R${produtoMaisBarato_preco}')
