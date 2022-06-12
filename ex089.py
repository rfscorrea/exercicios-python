"""Exercício Python 089: Crie um programa que leia nome e
duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita
que o usuário possa mostrar as notas de cada aluno individualmente."""

lista = []
while True:     # cadastrando alunos
    resposta = input('Adicionar mais um aluno? [s]/[n]: ')
    if resposta == 's':
        lista.append([input('Nome: '), float(input('Nota 1: ')), float(input('Nota 2: ')), 0.0])
    elif resposta == 'n':
        break

for aluno in range(0, len(lista)):      # atribuíndo as médias e as exibindo
    lista[aluno][3] = (lista[aluno][1] + lista[aluno][2]) / 2
    print(f'Aluno: {lista[aluno][0]}'
          f'\nMédia: {lista[aluno][3]}\n')

while True:
    resposta = input('Quer mostrar as notas de algum aluno? [s]/[n]: ')
    if resposta == 's':
        resposta = int(input(f'Qual aluno? [de 0 a {len(lista)-1}]: '))
        print(f'Aluno: {lista[resposta][0]}'
              f'\nNota 1: {lista[resposta][1]}'
              f'\nNota 2: {lista[resposta][2]}\n')
    elif resposta == 'n':
        break
