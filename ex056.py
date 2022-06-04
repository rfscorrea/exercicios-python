"""Exercício Python 056: Desenvolva um programa que leia o nome,
idade e sexo de 4 pessoas. No final do programa, mostre: a média de
idade do grupo, qual é o nome do homem mais velho e quantas mulheres
têm menos de 20 anos."""

nome = str('')
sexo = str('')
idade = int(0)
somaIdade = int(0)
mulheres = int(0)
nomeVelho = str('').strip().capitalize()
idadeVelho = int(0)
for c in range(0, 4):
    nome = str(input('Nome: ')).split()
    sexo = str(input('Sexo [m] / [f]: ')).lower().strip()
    idade = int(input('Idade: '))
    somaIdade += idade
    if sexo == 'm':
        if idade > idadeVelho:
            nomeVelho = nome
            idadeVelho = idade
    elif sexo == 'f':
        if idade < 20:
            mulheres += 1
media = int(somaIdade / 4)
print('A média de idade é: {} \nO nome do homem mais velho é: {} '
      '\nHá {} mulheres com menos de 20 anos'.format(media, nomeVelho, mulheres))
