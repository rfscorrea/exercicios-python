"""Exercício Python 094: Crie um programa que leia nome,
sexo e idade de várias pessoas, guardando os dados de cada
pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre:

A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média"""

from operator import itemgetter

lista = list()
listaMulheres = list()
listaIdadeAcimaMedia = list()
pessoasCadastradas = 0
somaIdades = 0
while True:
    resposta = input('Deseja cadastrar mais uma pessoa? [s]/[n]: ')
    if resposta == 's':
        nome = input('Nome: ')
        sexo = input('Sexo [m]/[f]: ')
        idade = int(input('Idade: '))
        somaIdades += idade
        dicionario = {'nome': nome, 'sexo': sexo, 'idade': idade}
        lista.append(dicionario)
        pessoasCadastradas += 1
    elif resposta == 'n':
        mediaIdades = float(somaIdades / pessoasCadastradas)
        break

for c in range(0, pessoasCadastradas):
    if lista[c]['sexo'] == 'f':
        listaMulheres.append(lista[c]['nome'])
    if lista[c]['idade'] > mediaIdades:
        listaIdadeAcimaMedia.append(lista[c]['nome'])

print(f'Foram cadastradas {pessoasCadastradas} pessoas'
      f'\nA média de idades é {mediaIdades:.2f}'
      f'\nLista com as mulheres: {listaMulheres}'
      f'\nLista pessoas idade acima média: {listaIdadeAcimaMedia}')
