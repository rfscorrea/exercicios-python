"""Exercício Python 090: Faça um programa que leia nome e média
de um aluno, guardando também a situação em um dicionário. No final,
mostre o conteúdo da estrutura na tela."""
nome = input('Nome: ')
media = float(input('Média: '))
dicio = {'nome': nome, 'media': media}
print(dicio.items())

