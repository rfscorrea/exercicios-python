"""Exercício Python 024: Crie um programa que leia o nome de uma
cidade diga se ela começa ou não com o nome 'SANTO' """

cidade = str(input('Nome da cidade: '))
cidadeFormatada = cidade.strip().lower().split()
nomeCidade = cidade.strip().title()
teste = cidadeFormatada[0] == 'santo'
print('Nome da cidade: {}'.format(nomeCidade))
print('O nome da cidade começa com "Santo?" \n{} '.format(teste))
